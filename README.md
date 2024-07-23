# Restaurante
 this is a restaurant type app for management of delivery and personel

Descripción de la Aplicación
La aplicación permite gestionar una lista de clientes y comidas. Cada cliente tiene un id, un nombre y una direccion. Cada comida tiene un id, un nombre y un precio. La aplicación ofrece las siguientes funcionalidades:

Listar clientes: Muestra todos los clientes registrados en el sistema.
Añadir cliente: Permite agregar un nuevo cliente solicitando su nombre y dirección.
Listar comidas: Muestra todas las comidas registradas en el sistema.
Añadir comida: Permite agregar una nueva comida solicitando su nombre y precio.
Estructura del Proyecto
El proyecto está organizado en los siguientes módulos y clases:

Modelos (Model)
Cliente: Representa a un cliente con id, nombre y direccion.
Comida: Representa a una comida con id, nombre y precio.
Repositorios (Repository)
ClienteRepositorio: Maneja la persistencia de los datos de clientes en un archivo CSV.
ComidaRepositorio: Maneja la persistencia de los datos de comidas en un archivo CSV.
Controladores (Controller)
ClientesControlador: Gestiona la lógica de negocio para los clientes.
ComidasControlador: Gestiona la lógica de negocio para las comidas.
Vistas (View)
ClientesVista: Interactúa con el usuario para las operaciones relacionadas con los clientes.
ComidasVista: Interactúa con el usuario para las operaciones relacionadas con las comidas.

Archivo main, que va a ejecutar toda la app.
