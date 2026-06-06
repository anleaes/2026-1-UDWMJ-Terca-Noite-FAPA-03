function maskCPF(value) {
  return value
    .replace(/\D/g, '')
    .slice(0, 11)
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
}

function isValidCPF(value) {
  const digits = value.replace(/\D/g, '');
  if (digits.length !== 11 || /^(\d)\1{10}$/.test(digits)) return false;

  let sum = 0;
  for (let i = 0; i < 9; i++) sum += parseInt(digits[i]) * (10 - i);
  let remainder = (sum * 10) % 11;
  if (remainder === 10 || remainder === 11) remainder = 0;
  if (remainder !== parseInt(digits[9])) return false;

  sum = 0;
  for (let i = 0; i < 10; i++) sum += parseInt(digits[i]) * (11 - i);
  remainder = (sum * 10) % 11;
  if (remainder === 10 || remainder === 11) remainder = 0;
  return remainder === parseInt(digits[10]);
}

function setupCPFField(inputId) {
  const input = document.getElementById(inputId);
  if (!input) return;

  input.setAttribute('maxlength', '14');
  input.setAttribute('inputmode', 'numeric');

  input.addEventListener('input', function () {
    const cursor = this.selectionStart;
    const prevLen = this.value.length;
    this.value = maskCPF(this.value);
    const diff = this.value.length - prevLen;
    this.setSelectionRange(cursor + diff, cursor + diff);
    validateCPFField(this);
  });

  input.addEventListener('blur', function () {
    validateCPFField(this);
  });
}

function validateCPFField(input) {
  const digits = input.value.replace(/\D/g, '');
  if (digits.length === 0) {
    input.classList.remove('is-valid', 'is-invalid');
    return;
  }
  if (isValidCPF(input.value)) {
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');
  } else {
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
  }
}
