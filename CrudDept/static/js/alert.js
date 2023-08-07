(function(){
    const btnEliminar = document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro elimimar el Departamento?');
            if(!confirmacion){
                e.preventDefault();
        }
    })
});

})();
