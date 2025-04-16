(() => {
    const results = [];
    document.querySelectorAll('table.dataTable tbody tr:not(.totals)').forEach(row => {
        const ship = row.querySelector('td.key.bold span.tooltip')?.textContent?.trim();
        const battles = parseFloat(row.querySelector('td:nth-child(7) span.tooltip')?.textContent?.trim().replace(/,/g, ''));
        const players = parseFloat(row.querySelector('td:nth-child(6) span.tooltip')?.textContent?.trim().replace(/,/g, ''));
        const winRate = battles / players;
        if (ship && battles && winRate) results.push({ ship, battles, winRate });
    });
    console.log('Final Results:', results);
    return results;
})();