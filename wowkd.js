(() => {
    const results = [];
    document.querySelectorAll('table.dataTable tbody tr:not(.totals)').forEach(row => {
        const ship = row.querySelector('td.key.bold span.tooltip')?.textContent?.trim();
        const battles = parseFloat(row.querySelector('td:nth-child(7) span.tooltip')?.textContent?.trim().replace(/,/g, ''));
        const kills = parseFloat(row.querySelector('td:nth-child(10) span.tooltip')?.textContent?.trim().replace('%', ''));
        const surv = parseFloat(row.querySelector('td:nth-child(17) span.tooltip')?.textContent?.trim().replace('%', ''));
        const winRate = kills / (1 - surv / 100);
        if (ship && battles && winRate) results.push({ ship, battles, winRate });
    });
    console.log('Final Results:', results);
    return results;
})();