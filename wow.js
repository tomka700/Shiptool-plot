(() => {
    const results = [];
    document.querySelectorAll('table.dataTable tbody tr:not(.totals)').forEach(row => {
        const ship = row.querySelector('td.key.bold span.tooltip')?.textContent?.trim();
        const battles = parseFloat(row.querySelector('td:nth-child(7) span.tooltip')?.textContent?.trim().replace(/,/g, ''));
        const winRate = parseFloat(row.querySelector('td:nth-child(11) span.tooltip')?.textContent?.trim().replace('%', ''));
        if (ship && battles && winRate) results.push({ ship, battles, winRate });
    });
    console.log('Final Results:', results);
    return results;
})();