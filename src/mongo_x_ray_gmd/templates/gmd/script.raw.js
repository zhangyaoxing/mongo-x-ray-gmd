charts = charts || [];

hljs.addPlugin(new CopyButtonPlugin({
    hook: (_, el) => el.textContent,
    callback: function () { return false; }
}));

window.onload = function () {
    hljs.highlightAll();
    addTableCopyButtons();
    // The outline, the outline toggle and the table copy buttons come from the
    // core scripts (post_outline.js / post_table_copy.js); this handler only
    // keeps the charts sized when the window or the outline changes.
    window.addEventListener('resize', function () {
        requestAnimationFrame(function () {
            for (var i = 0; i < charts.length; i++) {
                charts[i].resize();
            }
        });
    });
};
