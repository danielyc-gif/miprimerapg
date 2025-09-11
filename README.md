# 🗂️ Gestor de Tareas Minimalista

Un gestor de tareas elegante y minimalista construido con Flask, inspirado en el diseño de Apple.

![Gestor de Tareas](https://img.shields.io/badge/Flask-3.1.2-green) ![Python](https://img.shields.io/badge/Python-3.13.1-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Características

- 🎨 **Diseño minimalista** tipo Apple con efecto cristal (glassmorphism)
- 🌙 **Modo oscuro/claro** con toggle automático
- 📱 **Responsive design** para móviles y desktop
- ⚡ **Interfaz intuitiva** con animaciones suaves
- 💾 **Persistencia de datos** en archivo JSON
- ♿ **Accesibilidad completa** con ARIA labels

## 🚀 Instalación

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/gestor-tareas.git
   cd gestor-tareas
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

4. **Abre tu navegador**
   ```
   http://localhost:5000
   ```

## 🎯 Uso

### Funcionalidades principales

- **Agregar tareas**: Escribe en el campo de texto y presiona Enter o haz clic en "Agregar"
- **Completar tareas**: Haz clic en el texto de la tarea para marcarla como completada
- **Eliminar tareas**: Haz clic en el botón 🗑️ para eliminar una tarea
- **Cambiar tema**: Usa el botón 🌙/☀️ en la esquina superior derecha

### Atajos de teclado

- **Enter**: Agregar nueva tarea
- **Enter/Espacio**: Completar tarea (cuando está enfocada)

## 🛠️ Tecnologías utilizadas

- **Backend**: Flask 3.1.2
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Estilos**: CSS personalizado con efecto glassmorphism
- **Almacenamiento**: JSON local
- **Fuentes**: SF Pro Display (sistema Apple)

## 📁 Estructura del proyecto

```
gestor-tareas/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── templates/
│   └── index.html        # Plantilla HTML principal
├── .gitignore            # Archivos ignorados por Git
└── README.md             # Este archivo
```

## 🎨 Personalización

### Cambiar colores

Los colores se pueden personalizar editando las variables CSS en `templates/index.html`:

```css
/* Modo claro */
body {
  background: #ffffff;
  color: #1d1d1f;
}

/* Modo oscuro */
body.dark-mode {
  background: #000000;
  color: #ffffff;
}
```

### Agregar nuevas funcionalidades

1. **Nuevas rutas**: Agrega en `app.py`
2. **Nuevos estilos**: Modifica `templates/index.html`
3. **Nueva funcionalidad**: Actualiza tanto backend como frontend

## 🚀 Despliegue

### Heroku

1. Crea un archivo `Procfile`:
   ```
   web: python app.py
   ```

2. Despliega en Heroku:
   ```bash
   git push heroku main
   ```

### Vercel

1. Crea `vercel.json`:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Carlos Yam**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: tu-email@ejemplo.com

## 🙏 Agradecimientos

- Inspirado en el diseño minimalista de Apple
- Efecto glassmorphism para un look moderno
- Comunidad de Flask por la documentación

---

⭐ **¡Si te gusta este proyecto, dale una estrella en GitHub!** ⭐
