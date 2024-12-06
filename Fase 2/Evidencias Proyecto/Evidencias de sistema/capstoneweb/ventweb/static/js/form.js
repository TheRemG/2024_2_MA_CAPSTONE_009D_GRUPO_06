function validarRUT(rut) {

    //En primer lugar hace una limpieza del rut para que se calcule sin signos que comunmente se ocupan en el ingreso de RUT.
    const rutLimpio = rut.replace(/[.-]/g, '');
    if (rutLimpio.length < 8) return false;
    //Aqui se separa el rut en dos partes, los primeros 8 numeros en el cuerpo y luego el digito verificador.
    const cuerpo = rutLimpio.slice(0, -1);
    const digitoVerificador = rutLimpio.slice(-1).toUpperCase();
    //Cada dígito del cuerpo se multiplica por un multiplicador (inicialmente 2) y se acumula en suma. 
    //El multiplicador varía entre 2 y 7.
    let suma = 0;
    let multiplicador = 2;
    for (let i = cuerpo.length - 1; i >= 0; i--) {
        suma += parseInt(cuerpo[i]) * multiplicador;
        multiplicador = multiplicador < 7 ? multiplicador + 1 : 2;
    }
    //El digito verificador se calcula usando la variable anterior de suma.
    const dvCalculado = 11 - (suma % 11);
    //Si el digito verficador da 11 se transforma a 0 y si da 10 se transforma a "K"
    const dv = dvCalculado === 11 ? '0' : dvCalculado === 10 ? 'K' : dvCalculado.toString();
    //Si el digito verificador es igual al que se ingresó es true.
    return digitoVerificador === dv;
}