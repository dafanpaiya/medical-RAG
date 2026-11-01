/* Evidence-visibility rendering for the 医药RAG frontend.
 *
 * Renders ONLY structured fields returned by the backend. The frontend never infers
 * authority from titles, source names or page numbers: an unrecognized or missing
 * evidence_level renders an explicit unknown state, and citations without structured
 * attribution metadata are labelled as such.
 */
(function (root, factory) {
  'use strict';
  var api = factory();
  if (typeof module === 'object' && module && module.exports) {
    module.exports = api;
  }
  if (root) {
    root.escapeEvidenceHtml = api.escapeHtml;
    root.getEvidenceState = api.getEvidenceState;
    root.buildEvidenceBanner = api.buildEvidenceBanner;
    root.buildCitationsSection = api.buildCitationsSection;
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  var STATE_DEFINITIONS = {
    CANDIDATE_EVIDENCE_NON_AUTHORITATIVE: {
      state: 'candidate',
      tone: 'alert',
      icon: 'fa-triangle-exclamation',
      title: '非权威候选证据（CANDIDATE_ATTRIBUTION）',
      detail: '本结果包含非权威候选归因记录，不得作为已验证证据引用。'
    },
    RECOVERED_VERIFIED_EVIDENCE: {
      state: 'recovered',
      tone: 'warn',
      icon: 'fa-clock-rotate-left',
      title: '恢复血统验证归因（RECOVERED_VERIFIED_ATTRIBUTION）',
      detail: '该状态来自恢复流程的血统校验，不是自动验证；不得表述为已验证。'
    },
    VERIFIED_SOURCE_TEXT: {
      state: 'verified',
      tone: 'ok',
      icon: 'fa-circle-check',
      title: '已验证归因（VERIFIED_SOURCE_TEXT）',
      detail: '本次 ChP 引用均为已验证归因（VERIFIED_ATTRIBUTION）；该状态仅覆盖引用级归因。'
    },
    AUTHENTIC_SOURCE_TEXT: {
      state: 'authentic',
      tone: 'ok',
      icon: 'fa-shield-halved',
      title: '权威源文本（AUTHENTIC_SOURCE_TEXT）',
      detail: '后端返回结果级状态为权威源文本。'
    },
    CATALOG_NAVIGATION_ONLY: {
      state: 'catalog',
      tone: 'info',
      icon: 'fa-book',
      title: '仅编目指引（CATALOG_NAVIGATION_ONLY）',
      detail: '未检索到可引用的正文证据；以下仅为法定编目归属线索，不包含检验规格或限度数值。'
    },
    INSUFFICIENT_EVIDENCE_REFUSAL: {
      state: 'refusal',
      tone: 'neutral',
      icon: 'fa-circle-minus',
      title: '证据不足拒答（INSUFFICIENT_EVIDENCE_REFUSAL）',
      detail: '系统未检索到高于证据门槛的正文内容，已按零幻觉策略拒答。'
    },
    QUARANTINE_REFUSAL: {
      state: 'refusal',
      tone: 'neutral',
      icon: 'fa-circle-minus',
      title: '质量隔离拒答（QUARANTINE_REFUSAL）',
      detail: '命中的内容处于质量隔离状态，未被作为答案证据输出。'
    },
    UNSUPPORTED_PARAMETER_EVIDENCE_REFUSAL: {
      state: 'refusal',
      tone: 'warn',
      icon: 'fa-circle-minus',
      title: '证据不支持所问项目拒答（UNSUPPORTED_PARAMETER_EVIDENCE_REFUSAL）',
      detail: '检索到的正文证据未覆盖问题所询问的具体检验项目，已按零幻觉策略拒答，不以相邻项目或同类品种替代作答。'
    }
  };

  var TONES = {
    alert: {
      box: 'bg-red-50 border-red-400 text-red-900',
      icon: 'text-red-600'
    },
    warn: {
      box: 'bg-amber-50 border-amber-400 text-amber-900',
      icon: 'text-amber-600'
    },
    ok: {
      box: 'bg-emerald-50 border-emerald-300 text-emerald-900',
      icon: 'text-emerald-600'
    },
    info: {
      box: 'bg-blue-50 border-blue-300 text-blue-900',
      icon: 'text-blue-600'
    },
    neutral: {
      box: 'bg-gray-50 border-gray-300 text-gray-700',
      icon: 'text-gray-500'
    },
    unknown: {
      box: 'bg-gray-100 border-gray-400 text-gray-700',
      icon: 'text-gray-500'
    }
  };

  function escapeHtml(value) {
    if (value === null || value === undefined) return '';
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function getEvidenceState(result) {
    result = result || {};
    var level = typeof result.evidence_level === 'string' ? result.evidence_level : '';
    var citations = Array.isArray(result.citations) ? result.citations : [];
    if (Object.prototype.hasOwnProperty.call(STATE_DEFINITIONS, level)) {
      var def = STATE_DEFINITIONS[level];
      return {
        state: def.state,
        tone: def.tone,
        icon: def.icon,
        title: def.title,
        detail: def.detail,
        level: level,
        label: typeof result.evidence_label === 'string' ? result.evidence_label : '',
        summary: result.attribution_summary || null
      };
    }
    if (level) {
      return {
        state: 'unknown',
        tone: 'unknown',
        icon: 'fa-circle-question',
        title: '未识别的证据状态（unknown）',
        detail: '后端返回了本界面无法识别的证据状态值，按未知处理，不视为已验证。',
        level: level,
        label: '',
        summary: null
      };
    }
    if (citations.length) {
      return {
        state: 'unknown',
        tone: 'unknown',
        icon: 'fa-circle-question',
        title: '未提供结果级证据状态（unknown）',
        detail: '后端未返回 evidence_level，本界面无法确认结果是否经过验证，按未知处理。',
        level: '',
        label: '',
        summary: null
      };
    }
    return null;
  }

  function attributionSummaryText(summary) {
    if (!summary || typeof summary !== 'object' || Array.isArray(summary)) return '';
    var keys = Object.keys(summary).sort();
    if (!keys.length) return '';
    return keys.map(function (key) {
      return key + '=' + summary[key];
    }).join('；');
  }

  function buildEvidenceBanner(result) {
    var state = getEvidenceState(result);
    if (!state) return '';
    var tone = TONES[state.tone] || TONES.unknown;
    var role = state.tone === 'alert' ? 'alert' : 'status';
    var html = '<div class="evidence-banner ' + tone.box + ' border rounded-lg p-3 mb-3 text-sm" ' +
      'role="' + role + '" ' +
      'data-evidence-state="' + escapeHtml(state.state) + '" ' +
      'data-evidence-level="' + escapeHtml(state.level) + '">' +
      '<div class="flex items-start gap-2">' +
      '<i class="fas ' + tone.icon + ' mt-0.5"></i>' +
      '<div class="leading-relaxed">' +
      '<div class="font-bold">' + escapeHtml(state.title) + '</div>' +
      '<div class="mt-0.5">' + escapeHtml(state.detail) + '</div>';
    if (state.label) {
      html += '<div class="mt-1">后端标注：' + escapeHtml(state.label) + '</div>';
    }
    var summary = attributionSummaryText(state.summary);
    if (summary) {
      html += '<div class="mt-1">引用构成：' + escapeHtml(summary) + '</div>';
    }
    html += '</div></div></div>';
    return html;
  }

  function attributionLine(citation) {
    if (citation.attribution_status) {
      var authority;
      if (citation.is_authoritative === true) {
        authority = '是';
      } else if (citation.is_authoritative === false) {
        authority = '否（非权威候选）';
      } else {
        authority = '未提供（unknown）';
      }
      var basis = citation.authority_basis
        ? String(citation.authority_basis)
        : '未提供（unknown）';
      return '<div>归因状态：' + escapeHtml(citation.attribution_status) +
        '；权威性：' + escapeHtml(authority) +
        '；依据：' + escapeHtml(basis) + '</div>';
    }
    return '<div>归因状态：未提供（unknown）——后端未返回结构化归因字段，不得据此推定已验证。</div>';
  }

  function pagesLine(citation) {
    var hasPrinted = Array.isArray(citation.printed_pages);
    var hasPhysical = Array.isArray(citation.physical_pages);
    if (hasPrinted || hasPhysical) {
      var parts = [];
      if (hasPrinted) {
        parts.push('印刷页：' + (citation.printed_pages.length
          ? citation.printed_pages.map(String).join(', ')
          : '未提供（unknown）'));
      }
      if (hasPhysical) {
        parts.push('物理 PDF 页：' + (citation.physical_pages.length
          ? citation.physical_pages.map(String).join(', ')
          : '未提供（unknown）'));
      }
      return '<div>' + escapeHtml(parts.join('；')) + '</div>';
    }
    var pages = citation.pages;
    if (pages === undefined || pages === null || pages === '') {
      return '<div>页码：未提供（unknown）</div>';
    }
    var text = Array.isArray(pages) ? pages.join(', ') : String(pages);
    return '<div>页码：' + escapeHtml(text) + '（印刷/物理方案后端未标注，unknown）</div>';
  }

  function buildCitationCard(citation, index) {
    citation = citation || {};
    var isChp = citation.source_type === 'CHP2025';
    var sourceType = isChp ? 'CHP2025' : 'UNSPECIFIED';
    var badge = isChp ? 'ChP 2025 候选记录' : '企业法规库 / 未分类来源';
    var badgeClass = isChp
      ? 'bg-amber-100 text-amber-900 border-amber-300'
      : 'bg-gray-100 text-gray-700 border-gray-300';
    var title = citation.document || citation.doc_title_zh || citation.doc_title;
    var titleText = title ? String(title) : '未提供文档标题（unknown）';
    var lines = [];
    lines.push('<div>chunk_id：' + (citation.chunk_id
      ? escapeHtml(citation.chunk_id) : '未提供（unknown）') + '</div>');
    lines.push('<div>来源类型：' + escapeHtml(sourceType) + '</div>');
    lines.push(attributionLine(citation));
    lines.push(pagesLine(citation));
    if (citation.page_mapping_status) {
      lines.push('<div>页码范围核验：' + escapeHtml(citation.page_mapping_status) + '</div>');
    }
    if (citation.physical_volume) {
      lines.push('<div>卷：' + escapeHtml(citation.physical_volume) + '</div>');
    }
    if (citation.evidence_label) {
      lines.push('<div>后端标注：' + escapeHtml(citation.evidence_label) + '</div>');
    }
    return '<li class="citation-card rounded-lg border border-gray-200 bg-gray-50 p-3 text-xs text-gray-700 space-y-0.5" ' +
      'data-source-type="' + sourceType + '">' +
      '<div class="flex flex-wrap items-center gap-2 font-semibold text-gray-800">' +
      '<span class="px-1.5 py-0.5 rounded border text-[11px] ' + badgeClass + '">' +
      escapeHtml(badge) + '</span>' +
      '<span>[' + (index + 1) + '] ' + escapeHtml(titleText) + '</span>' +
      '</div>' + lines.join('') + '</li>';
  }

  function buildCitationsSection(result) {
    result = result || {};
    var citations = Array.isArray(result.citations) ? result.citations : [];
    var conflicts = Array.isArray(result.authority_conflicts) ? result.authority_conflicts : [];
    if (!citations.length && !conflicts.length) return '';
    var hasChp = citations.some(function (citation) {
      return citation && citation.source_type === 'CHP2025';
    });
    var hasUnspecified = citations.some(function (citation) {
      return citation && citation.source_type !== 'CHP2025';
    });
    var html = '<div class="citations-block mt-4 pt-3 border-t border-gray-200" data-testid="citations-section">' +
      '<div class="text-xs font-semibold text-gray-600 mb-2">' +
      '<i class="fas fa-book-open mr-1"></i>引用与证据状态（逐条呈现后端结构化字段）</div>';
    if (hasChp && hasUnspecified) {
      html += '<div class="mb-2 text-xs text-amber-800 bg-amber-50 border border-amber-200 rounded p-2">' +
        '混合来源结果：同时包含 ChP 2025 候选引用与企业法规库（或未提供来源类型）引用；' +
        '两者权威状态不同，请逐条核对，不得互相替代。</div>';
    }
    if (citations.length) {
      html += '<ol class="space-y-2">';
      citations.forEach(function (citation, index) {
        html += buildCitationCard(citation, index);
      });
      html += '</ol>';
    }
    if (conflicts.length) {
      html += '<div class="mt-3 text-xs bg-orange-50 border border-orange-200 rounded p-2 text-orange-900">' +
        '<div class="font-semibold mb-1">未裁决来源冲突（UNRESOLVED）</div><ul class="list-disc pl-4 space-y-0.5">';
      conflicts.forEach(function (conflict) {
        html += '<li>' + escapeHtml(conflict) + '</li>';
      });
      html += '</ul></div>';
    }
    html += '</div>';
    return html;
  }

  return {
    escapeHtml: escapeHtml,
    getEvidenceState: getEvidenceState,
    buildEvidenceBanner: buildEvidenceBanner,
    buildCitationsSection: buildCitationsSection
  };
});