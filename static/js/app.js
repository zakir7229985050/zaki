// App JS for interactive features
document.addEventListener('DOMContentLoaded', function() {
    // Video.js init
    var player = videojs('my-video', {
        responsive: true,
        fluid: true,
        controls: true,
        preload: 'auto'
    });

    // PDF.js viewer
    if (window.pdfViewer) {
        pdfjsLib.getDocument('/uploads/notes/sample.pdf').promise.then(function(pdf) {
            pdfViewer.pdfDoc = pdf;
            pdfViewer.pageNum = 1;
            pdfViewer.renderPage();
        });
    }

    // Modal forms etc.
    var uploadModals = document.querySelectorAll('[data-bs-toggle=\"modal\"]');
    uploadModals.forEach(modal => modal.addEventListener('click', function () {
        // AJAX upload logic
    }));

    // Role-based hide/show
    const role = localStorage.getItem('userRole');
    if (role) {
        document.body.classList.add(role.toLowerCase());
    }
});

