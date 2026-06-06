function maskPhone(value) {
  const digits = value.replace(/\D/g, '').slice(0, 11);
  if (digits.length <= 10) {
    return digits
      .replace(/(\d{2})(\d)/, '($1) $2')
      .replace(/(\d{4})(\d{1,4})$/, '$1-$2');
  }
  return digits
    .replace(/(\d{2})(\d)/, '($1) $2')
    .replace(/(\d{5})(\d{1,4})$/, '$1-$2');
}

function setupPhoneField(inputId) {
  const input = document.getElementById(inputId);
  if (!input) return;

  input.setAttribute('maxlength', '15');
  input.setAttribute('inputmode', 'numeric');

  input.addEventListener('input', function () {
    const cursor = this.selectionStart;
    const prevLen = this.value.length;
    this.value = maskPhone(this.value);
    const diff = this.value.length - prevLen;
    this.setSelectionRange(cursor + diff, cursor + diff);
  });
}
