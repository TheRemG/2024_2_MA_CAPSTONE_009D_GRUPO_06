function validarRUT(rut) {
    // Elimina puntos y guiones del RUT
    rut = rut.replace(/\./g, '').replace(/-/g, '');

    // Verifica la longitud correcta (mínimo 8 caracteres)
    if (!/^\d{7,8}[0-9Kk]$/.test(rut)) {
        return false;
    }

    // Separa el cuerpo del RUT y el dígito verificador (DV)
    const cuerpo = rut.slice(0, -1);
    const dvIngresado = rut.slice(-1).toUpperCase();

    // Cálculo del dígito verificador (algoritmo de módulo 11)
    let suma = 0;
    let multiplo = 2;

    for (let i = cuerpo.length - 1; i >= 0; i--) {
        suma += parseInt(cuerpo[i]) * multiplo;
        multiplo = multiplo === 7 ? 2 : multiplo + 1;
    }

    const dvEsperado = 11 - (suma % 11);
    const dvCalculado = dvEsperado === 11 ? '0' : dvEsperado === 10 ? 'K' : dvEsperado.toString();

    return dvIngresado === dvCalculado;
}