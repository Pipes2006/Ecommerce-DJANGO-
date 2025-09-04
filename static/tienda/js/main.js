
// Carrito de compras en localStorage
let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

function guardarCarrito() {
	localStorage.setItem('carrito', JSON.stringify(carrito));
}

function agregarAlCarrito(producto) {
	const existente = carrito.find(item => item.id === producto.id);
	if (existente) {
		// Sumar cantidad, sin pasar el stock
		let nuevaCantidad = existente.cantidad + producto.cantidad;
		existente.cantidad = nuevaCantidad > existente.stock ? existente.stock : nuevaCantidad;
	} else {
		carrito.push(producto);
	}
	guardarCarrito();
	alert('Producto agregado al carrito');
}

document.addEventListener('DOMContentLoaded', function() {
	document.querySelectorAll('.btn-agregar-carrito').forEach(function(btn) {
		btn.addEventListener('click', function() {
			const id = parseInt(this.dataset.id);
			const nombre = this.dataset.nombre;
			const precio = parseFloat(this.dataset.precio);
			const stock = parseInt(this.dataset.stock);
    			const imagen = this.dataset.imagen || '';
			const cantidadInput = document.getElementById('cantidad-' + id);
			let cantidad = parseInt(cantidadInput.value);
			if (isNaN(cantidad) || cantidad < 1) cantidad = 1;
			if (cantidad > stock) cantidad = stock;
			agregarAlCarrito({ id, nombre, precio, cantidad, stock, imagen });
		});
	});
});
