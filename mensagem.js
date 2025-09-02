document.getElementById('contato-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const formData = new FormData(this);

  fetch('https://seuservidor.com/api/mensagem', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (response.ok) {
      alert('Mensagem enviada com sucesso!');
    } else {
      alert('Erro ao enviar mensagem.');
    }

       #mensagem {
      color: black;
      background-color: white;
      font-size: 16px;
    }
  })
  .catch(error => {
    console.error('Erro ao enviar mensagem:', error);
  });
});


