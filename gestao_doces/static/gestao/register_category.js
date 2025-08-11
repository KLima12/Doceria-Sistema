document.addEventListener('DOMContentLoaded', function() {
    const input = document.querySelector('input[type="file"][name="imagem"]');
    const preview = document.getElementById('preview');
    if (input) {
        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                }
                reader.readAsDataURL(file);
            } else {
                preview.src = "";
            }
        });
    }
});
