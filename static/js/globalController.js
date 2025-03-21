
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add('animate__fadeOutRight');
            setTimeout(() => {
                alert.remove();
            }, 500);
        }, 5000);
    });    
});