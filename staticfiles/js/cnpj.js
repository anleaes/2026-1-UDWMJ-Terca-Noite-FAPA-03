function maskCNPJ(value) {
  return value
    .replace(/\D/g, '')
    .slice(0, 14)
    .replace(/(\d{2})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1/$2')
    .replace(/(\d{4})(\d{1,2})$/, '$1-$2');
}

function isValidCNPJ(value) {
  const digits = value.replace(/\D/g, '');
  if (digits.length !== 14 || /^(\d)\1{13}$/.test(digits)) return false;

  const calc = (d, len) => {
    let sum = 0;
    let pos = len - 7;
    for (let i = len; i >= 1; i--) {
      sum += parseInt(d[len - i]) * pos--;
      if (pos < 2) pos = 9;
    }
    const r = sum % 11;
    return r < 2 ? 0 : 11 - r;
  };

  return (
    calc(digits, 12) === parseInt(digits[12]) &&
    calc(digits, 13) === parseInt(digits[13])
  );
}

function setupCNPJField(inputId) {
  const input = document.getElementById(inputId);
  if (!input) return;

  input.setAttribute('maxlength', '18');
  input.setAttribute('inputmode', 'numeric');

  input.addEventListener('input', function () {
    const cursor = this.selectionStart;
    const prevLen = this.value.length;
    this.value = maskCNPJ(this.value);
    const diff = this.value.length - prevLen;
    this.setSelectionRange(cursor + diff, cursor + diff);
    validateCNPJField(this);
  });

  input.addEventListener('blur', function () {
    validateCNPJField(this);
  });
}

function validateCNPJField(input) {
  const digits = input.value.replace(/\D/g, '');
  if (digits.length === 0) {
    input.classList.remove('is-valid', 'is-invalid');
    return;
  }
  if (isValidCNPJ(input.value)) {
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');
  } else {
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
  }
}
