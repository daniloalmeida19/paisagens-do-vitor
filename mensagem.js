

  function validarFormulario() {
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();

    if (!nome || !email || !mensagem) {
      alert('⚠️ Por favor, preencha todos os campos antes de enviar.');
      return false;
    }

    // Mensagem de confirmação (opcional, já que FormSubmit redireciona)
    alert('✅ Obrigado, sua mensagem foi enviada com sucesso!');
    return true;
  }


    
   
  

