(function () {
    const btnDelete = document.querySelectorAll(".btn-delete");

    btnDelete.forEach(btn => {
        btn.addEventListener("click", (e) =>{
            const confirmation = confirm("Estas seguro de eliminar el usuario?");
            if(!confirmation){
                e.preventDefault();
            }
        });
    });
})();

