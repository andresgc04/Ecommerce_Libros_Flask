(function () {
  const btnsBuyBooks = document.querySelectorAll(".btnBuyBooks");

  let isbnBookSelected = null;

  const csrf_token = document.querySelector("[name='csrf-token']").value;

  const confirmPurchase = async () => {
    await fetch("http://127.0.0.1:5000/buyBook", {
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
          console.error("Error!!");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Libro Comprado!!");
      })
      .catch((error) => {
        console.error(`Error: ${error}`);
      });
  };

  btnsBuyBooks.forEach((btn) => {
    btn.addEventListener("click", function () {
      isbnBookSelected = this.id;

      confirmPurchase();
    });
  });
})();
