# Sistema_de_Corretaje
Sistema web CRM (Corretaje) para mmcontaprop 

# Prototipo MMCONTAPROP SPA - Sistema Inmobiliario

Este repositorio contiene el prototipo de interfaz web (Frontend estático) para la solución informática de la corredora de propiedades **MMCONTAPROP SPA**, desarrollado como parte de la evaluación de la Unidad 2 de la asignatura **Proyecto Integrado (TIHI43)**.

---

## 1. Integrantes del Equipo

* **Sebastián Ferreira** — GitHub: `@Theluxito`
* **Yorbyn Mollo**       — GitHub: `@yorbyn`
* **Josué Araya**        — GitHub: `@Peschke`

---

## 2. Tecnologías y Frameworks
* **Lenguajes:**            HTML5, CSS3
* **Framework de Estilos:** Bootstrap 5 

---

## 3. Tabla de Gestores y Asignación de Historias de Usuario

Las 30 Historias de Usuario (HU) definidas en la Unidad 1 se han organizado en gestores del sistema y repartido de manera equitativa entre los tres integrantes (cumpliendo con la regla de tolerancia máxima de 2 HU entre integrantes):

| Gestor del Sistema                        | Historias Incluidas           | N° HU | Responsable        | Rama en Git         |
|-------------------------------------------|-------------------------------|-------|--------------------|---------------------|
| **Gestor 1: Acceso y Propietarios**       | HU-01 a HU-07, HU-09          |   8   | Sebastián Ferreira | `feature/sferreira` |
| **Gestor 2: Documentos y Bitácora**       | HU-04, HU-05                  |   2   | Sebastián Ferreira | `feature/sferreira` |
| **Gestor 3: Inventario de Propiedades**   | HU-08, HU-10 a HU-17, HU-20   |   10  | Yorbyn Mollo       | `feature/ymollo`    |
| **Gestor 4: Portal Web y Búsqueda**       | HU-18, HU-21 a HU-26          |   7   | Josué Araya        | `feature/jaraya`    |
| **Gestor 5: Ficha Pública y Detalle**     | HU-27 a HU-30                 |   3   | Josué Araya        | `feature/jaraya`    |

* **Total Sebastián Ferreira:** 10 HUs
* **Total Yorbyn Mollo:**       10 HUs
* **Total Josué Araya:**        10 HUs

---

## 4. Estructura de Pantallas y Archivos HTML por Responsable

Para evitar conflictos de integración (*merge conflicts*) en Git, la maquetación se distribuye en archivos HTML independientes por pantalla:

###  Sebastián Ferreira (`feature/sferreira`) — 10 HUs
* **`login.html`** *(HU-07)*: Formulario de inicio de sesión administrativo.
* **`propietarios.html`** *(HU-06)*: Listado y búsqueda de propietarios por RUT o Nombre.
* **`nuevo-propietario.html`** *(HU-01, HU-02, HU-03, HU-09)*: Formulario de alta/edición de propietarios con dirección confidencial.
* **`detalle-propietario.html`** *(HU-04, HU-05)*: Módulo para adjuntar documentos PDF/imágenes y registro de notas en bitácora.

---

###  Yorbyn Mollo (`feature/ymollo`) — 10 HUs + Maquetación CSS Global
* **`styles.css`**: Hoja de estilos global, paleta corporativa y componentes Bootstrap.
* **`nueva-propiedad.html`** *(HU-08, HU-10, HU-11, HU-12, HU-13, HU-16, HU-17)*: Formulario de alta de inmuebles con precio obligatorio, tipo de operación y características.
* **`galeria-propiedad.html`** *(HU-14, HU-15)*: Carga multimedia de fotografías y enlace a video comercial.
* **`editar-propiedad.html`** *(HU-20)*: Edición comercial y cambio de estado a Vendida/Arrendada.

---

###  Josué Araya (`feature/jaraya`) — 10 HUs
* **`index.html`** *(HU-21, HU-22, HU-23, HU-24, HU-25, HU-26)*: Portada pública del catálogo con barra de filtros combinados por precio, tipo y dormitorios.
* **`inventario-crm.html`** *(HU-18)*: Grilla/tabla privada de administración del inventario dentro del CRM.
* **`ficha-propiedad.html`** *(HU-27, HU-28, HU-29, HU-30)*: Ficha comercial pública con carrusel de imágenes y protección de datos sensibles.

---

## 5. Normas de Versionamiento y Convención de Commits

1. **Estructura de Ramas:**
   * `main`: Contiene únicamente la versión estable probada del prototipo.
   * `develop`: Rama de integración y pruebas de pantallas en conjunto.
   * `feature/<inicial_nombre><apellido>`: Rama personal e individual por integrante.
   * *Queda estrictamente prohibido hacer commits directos sobre `main` o `develop`*.

2. **Formato de Commits Atómicos:**
   * `feat(HU-XX): <descripción del cambio en presente>`
   * `style(HU-XX): <cambios estéticos, tipografía o responsividad>`
   * `fix(HU-XX): <corrección de enlaces o errores>`
   * `docs: <actualizaciones en documentación o README>`

3. **Flujo de Integración (Pull Requests):**
   * Se realizan Pull Requests parciales desde la rama personal hacia `develop` por grupos de 2 a 5 HUs.
   * Todo Pull Request debe ser revisado, comentado y aprobado por otro integrante del equipo (prohibida la auto-aprobación).
   * Se realizarán al menos dos Pull Requests consolidados de `develop` hacia `main` durante el periodo de desarrollo.