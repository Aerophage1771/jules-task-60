/* Preview-only copy of what the live site's article reader (client/src/sunlit/public/blog/articleContent.tsx)
 * does to a post body: heading ids and the "On this page" panel, scrollable reference tables with
 * data-label cells, and outside links opening in a new tab. The post HTML itself stays exactly as it
 * will be stored in the post's `content` field. */
(function () {
  function prepare() {
    var meta = {};
    try { meta = JSON.parse(document.getElementById('post-meta').textContent); } catch (e) {}
    var slug = meta.slug || 'post';
    var body = document.querySelector('.a-prose');
    var nav = document.querySelector('.a-toc nav');
    if (!body) return;
    var headings = body.querySelectorAll('h2, h3');
    headings.forEach(function (h, i) {
      var id = 'article-' + slug + '/s' + (i + 1);
      h.id = id; h.setAttribute('tabindex', '-1');
      if (nav) {
        var a = document.createElement('a');
        a.href = '#' + id; a.textContent = h.textContent;
        if (h.tagName === 'H3') a.className = 'sub';
        if (i === 0) a.setAttribute('aria-current', 'true');
        nav.appendChild(a);
      }
    });
    body.querySelectorAll('table').forEach(function (table, index) {
      if (table.parentElement.classList.contains('a-table')) return;
      var columns = Array.prototype.map.call(table.querySelectorAll('thead th'), function (c) { return c.textContent.trim(); });
      var wrap = document.createElement('div');
      wrap.className = 'a-table' + (columns.length > 3 ? ' wide' : columns.length ? ' stack' : '');
      wrap.setAttribute('tabindex', '0'); wrap.setAttribute('role', 'region');
      wrap.setAttribute('aria-label', 'Reference table ' + (index + 1) + '. Scroll horizontally to read all columns.');
      table.parentNode.insertBefore(wrap, table); wrap.appendChild(table);
      table.querySelectorAll('th').forEach(function (c) { c.setAttribute('scope', 'col'); });
      table.querySelectorAll('tbody tr').forEach(function (row) {
        var col = 0;
        Array.prototype.forEach.call(row.children, function (cell) {
          if (columns[col] && !cell.hasAttribute('data-label')) cell.setAttribute('data-label', columns[col]);
          col += Number(cell.getAttribute('colspan')) || 1;
        });
      });
    });
    body.querySelectorAll('a[href]').forEach(function (a) {
      try {
        var url = new URL(a.getAttribute('href'), 'https://germainetutoring.com');
        if (!/(^|\.)germainetutoring\.com$/.test(url.hostname)) { a.target = '_blank'; a.rel = 'noopener noreferrer'; }
      } catch (e) {}
    });
    var when = document.querySelector('.b-meta time');
    if (when && meta.date) when.textContent = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' }).format(new Date(meta.date + 'T12:00:00Z'));
    var mins = document.querySelector('.b-meta .read');
    if (mins) {
      var words = body.textContent.trim().split(/\s+/).length;
      mins.textContent = (meta.readTime || Math.max(1, Math.ceil(words / 230))) + ' min read';
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', prepare); else prepare();
})();
