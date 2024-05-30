document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.getElementById('filter-form');
    if (filterForm) {
        filterForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const category = document.getElementById('category-filter').value;
            const season = document.getElementById('season-filter').value;
            let url = '/';
            if (category) {
                url += 'category/' + category;
            }
            if (season) {
                url += 'season/' + season;
            }
            window.location.href = url;
        });
    }
});
