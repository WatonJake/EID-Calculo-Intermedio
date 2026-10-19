# Grupo 1: Construcción de una suma de Riemann

Proyecto de Cálculo Intermedio: una animación con Manim Community para explicar
cómo se aproxima una región bajo una curva mediante una suma de áreas de
rectángulos.

**Pregunta central:** ¿Cómo se transforma una región bajo una curva en una suma
de áreas de rectángulos?

## Contenido del repositorio

- `Suma_De_Riemann.py`: código fuente de la escena
  `ConstruccionSumaRiemann`.
- `README.md`: instrucciones para configurar el entorno y renderizar la escena.

## Ejemplo matemático

La animación considera (f(x)=x^2) en ([0,2]), con (n=4) subintervalos
iguales. Usa puntos medios como puntos muestra, de modo que
\(\Delta x=(2-0)/4=1/2\). Primero destaca un rectángulo y muestra su altura
\(f(x_3^*)=25/16\) y su aporte de área \(f(x_3^*)\Delta x=25/32\). Luego
construye la suma completa:

\[
S_4=\sum_{i=1}^{4} f(x_i^*)\Delta x
=\frac{1+9+25+49}{32}
=\frac{21}{8}=2.625.
\]

La escena compara esta aproximación con el área exacta
\(\int_0^2 x^2\,dx=8/3\) y muestra cómo se refina la partición al aumentar
\(n\). El límite de las sumas de Riemann es la integral definida.

## Requisitos

- Windows 10/11.
- Python 3.12.
- Manim Community Edition 0.22.0.
- FFmpeg, disponible en el `PATH`.
- Una distribución LaTeX, como MiKTeX, y `dvisvgm`, disponibles en el `PATH`.

FFmpeg se utiliza para crear el video. LaTeX y `dvisvgm` permiten a Manim
generar las fórmulas matemáticas.

## Instalación

Abre PowerShell en la carpeta del proyecto:

```powershell
cd "C:\Users\Camilo\Documents\Calculo 2"
```

### Python y Manim

Crea y activa un entorno virtual:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install manim==0.22.0
```

Si PowerShell bloquea la activación, instala Manim usando directamente el
Python del entorno:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install manim==0.22.0
```

### FFmpeg

Si no está instalado, puedes instalarlo con WinGet:

```powershell
winget install --id Gyan.FFmpeg.Shared -e
```

También puedes seguir las instrucciones de instalación de
[FFmpeg](https://ffmpeg.org/download.html). Comprueba que `ffmpeg` esté en el
`PATH`.

### MiKTeX y dvisvgm

1. Instala [MiKTeX](https://miktex.org/download).
2. Abre MiKTeX Console y comprueba que esté actualizado.
3. Instala el paquete `dvisvgm` desde **Packages** si no está presente.
4. Permite que MiKTeX instale los paquetes que falten durante el primer render.
   Por ejemplo, si solicita `preview.sty`, pulsa **Install**.
5. Cierra y vuelve a abrir PowerShell para actualizar el `PATH`.

## Comprobar las dependencias

Activa `.venv` y ejecuta:

```powershell
python --version
manim --version
ffmpeg -version
latex --version
dvisvgm --version
```

Manim debería indicar `v0.22.0`; los demás comandos deben mostrar sus
respectivas versiones.

## Renderizar la escena

Desde la carpeta del proyecto, con `.venv` activado:

```powershell
manim -pql .\Suma_De_Riemann.py ConstruccionSumaRiemann
```

`-p` abre el video al terminar y `-ql` genera una versión de calidad baja para
probar la escena rápidamente. Para renderizar en calidad alta:

```powershell
manim -pqh .\Suma_De_Riemann.py ConstruccionSumaRiemann
```

Manim genera el MP4 bajo una ruta similar a:

```text
media\videos\Suma_De_Riemann\1080p60\ConstruccionSumaRiemann.mp4
```

La carpeta y el subdirectorio de calidad se crean al renderizar. No hace falta
conservar los videos anteriores para volver a generar la escena.

## Fuentes matemáticas

Fuentes consultadas para preparar la explicación:

- Wikipedia, colaboradores. [«Suma de Riemann»](https://es.wikipedia.org/wiki/Suma_de_Riemann).
- Khan Academy. [“Riemann sums review”](https://es.khanacademy.org/math/ap-calculus-ab/ab-integration-new/ab-6-2/a/riemann-sums-review).
- Universidad de Chile, recurso Suma y Sigue. [*Apunte: Sumas de Riemann e integral definida*](https://static.sumaysigue.uchile.cl/disponibilizacion_aula360/LDI/U4%20-%20Comprender%20la%20integral%20como%20proceso%20de%20reversibilidad%20y%20c%C3%A1lculo%20de%20%C3%A1reas/T1%20-%20Nociones%20de%20integraci%C3%B3n/C2%20-%20Sumas%20de%20Riemann%20e%20integral%20definida/Apunte%20-%20Sumas%20de%20Riemann%20e%20integral%20definida.pdf).

## Herramientas y declaración de IA

- La animación se genera con **Manim Community Edition**. Documentación:
  [docs.manim.community](https://docs.manim.community/en/stable/).
- Se utilizó **Copilot** como asistente de IA para apoyar la creación y revisión
  del código Manim y de este README. 

## Datos del grupo

Completar antes de la entrega:

- Curso: `MAT1188`
- Grupo: `G01`
- Integrantes y cuentas de GitHub: `Camilo Gangas (WatonJake) Benjamin Parra (Laantiii) Fabian Gracia (Fabo01)`
- Repositorio: `https://github.com/WatonJake/EID-Calculo-Intermedio`
- SHA del commit que corresponde al código del video: `f62c0712bc2a4fb663e2101aa1c3de1865af99cc`
