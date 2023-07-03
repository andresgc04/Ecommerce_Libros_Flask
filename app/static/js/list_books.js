(function () {
  const btnsBuyBooks = document.querySelectorAll(".btnBuyBooks");

  let isbnBookSelected = null;

  const csrf_token = document.querySelector("[name='csrf-token']").value;

  const confirmPurchase = () => {
    Swal.fire({
      title: "¿Confirmar la compra del libro seleccionado?",
      inputAttributes: {
        autocapitalize: "off",
      },
      showCancelButton: true,
      confirmButtonText: "Comprar",
      showLoaderOnConfirm: true,
      preConfirm: async () => {
        return await fetch(`${window.origin}/buyBook`, {
          method: "POST",
          mode: "same-origin",
          credentials: "same-origin",
          headers: {
            "Content-Type": "application/json",
            "X-CSRF-TOKEN": csrf_token,
          },
          body: JSON.stringify({
            isbn: isbnBookSelected,
          }),
        })
          .then((response) => {
            if (!response.ok) {
              notificationSwal("Error", response.statusText, "error", "Cerrar");
            }
            return response.json();
          })
          .then((data) => {
            notificationSwal("¡Éxito!", 'Libro Comprado', "success", "¡Ok!");
          })
          .catch((error) => {
            notificationSwal("Error", error, "error", "Cerrar");
          });
      },
      allowOutsideClick: () => false,
      allowEscapeKey: () => false,
    });
  };

  btnsBuyBooks.forEach((btn) => {
    btn.addEventListener("click", function () {
      isbnBookSelected = this.id;

      confirmPurchase();
    });
  });
})();
