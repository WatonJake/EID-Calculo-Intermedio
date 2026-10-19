from manim import *


class ConstruccionSumaRiemann(Scene):
    def construct(self):

        # ---------------------------------------------------------
        # DATOS DEL EJEMPLO
        # ---------------------------------------------------------

        a = 0
        b = 2
        n = 4

        f = lambda x: x**2

        dx = (b - a) / n

        samples = [
            a + (i + 0.5) * dx
            for i in range(n)
        ]

        sample_index = 2
        sample_x = samples[sample_index]

        # ---------------------------------------------------------
        # TÍTULO
        # ---------------------------------------------------------

        title = Text(
            "Construcción de una suma de Riemann",
            font_size=34
        )

        title.to_edge(UP, buff=0.20)

        self.play(Write(title))
        self.wait(1)

        interval = MathTex(
            r"f(x)=x^2,\qquad [a,b]=[0,2]",
            font_size=30
        )

        interval.next_to(title, DOWN, buff=0.18)

        self.play(Write(interval))
        self.wait(1)

        # ---------------------------------------------------------
        # EJES Y FUNCIÓN
        # ---------------------------------------------------------

        axes = Axes(
            x_range=[0, 2, 0.5],
            y_range=[0, 4, 1],
            x_length=5.4,
            y_length=3.8,
            tips=False,
            axis_config={
                "include_numbers": True,
                "font_size": 20
            }
        )

        axes.shift(LEFT * 2.8 + DOWN * 0.55)

        curve = axes.plot(
            f,
            x_range=[0, 2],
            color=BLUE,
            stroke_width=4
        )

        curve.set_z_index(5)

        graph_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=26),
            y_label=MathTex("f(x)", font_size=26)
        )

        self.play(
            Create(axes),
            Create(curve),
            FadeIn(graph_labels)
        )

        self.wait(2)

        # ---------------------------------------------------------
        # REGIÓN BAJO LA CURVA
        # ---------------------------------------------------------

        area = axes.get_area(
            curve,
            x_range=[0, 2],
            color=BLUE,
            opacity=0.22
        )

        area.set_z_index(0)

        area_text = VGroup(
            Text(
                "Región bajo la curva",
                font_size=23
            ),
            MathTex(
                r"0\leq x\leq 2",
                font_size=25
            )
        ).arrange(
            DOWN,
            buff=0.15
        )

        area_text.move_to(
            RIGHT * 3.05 + UP * 1.05
        )

        self.play(
            FadeIn(area),
            Write(area_text)
        )

        self.wait(3)

        # ---------------------------------------------------------
        # SECCIÓN 1 — PARTICIÓN
        # ---------------------------------------------------------

        self.play(FadeOut(area_text))

        partition_text = VGroup(
            Text(
                "Dividimos el intervalo en 4 partes iguales.",
                font_size=21
            ),
            MathTex(
                r"n=4",
                font_size=27
            ),
            MathTex(
                r"\Delta x="
                r"\frac{b-a}{n}"
                r"="
                r"\frac{2-0}{4}"
                r"="
                r"\frac12",
                font_size=27
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.24
        )

        partition_text.move_to(
            RIGHT * 3.1 + UP * 0.9
        )

        self.play(Write(partition_text[0]))
        self.wait(1)

        # Líneas de partición interiores
        partition_lines = VGroup()

        for i in range(1, n):
            x = a + i * dx

            line = DashedLine(
                axes.c2p(x, 0),
                axes.c2p(x, 4),
                dash_length=0.07,
                stroke_width=1.5,
                color=GREY_B
            )

            partition_lines.add(line)

        self.play(
            LaggedStart(
                *[
                    Create(line)
                    for line in partition_lines
                ],
                lag_ratio=0.25
            )
        )

        self.play(Write(partition_text[1]))
        self.play(Write(partition_text[2]))

        self.wait(2)

        # ---------------------------------------------------------
        # MOSTRAR Δx
        # ---------------------------------------------------------

        dx_arrow = DoubleArrow(
            axes.c2p(0, 0) + DOWN * 0.45,
            axes.c2p(0.5, 0) + DOWN * 0.45,
            buff=0,
            color=YELLOW,
            stroke_width=2,
            tip_length=0.12
        )

        dx_label = MathTex(
            r"\Delta x=\frac12",
            font_size=23,
            color=YELLOW
        )

        dx_label.next_to(
            dx_arrow,
            DOWN,
            buff=0.07
        )

        self.play(
            GrowFromCenter(dx_arrow),
            Write(dx_label)
        )

        self.wait(2)

        # ---------------------------------------------------------
        # SECCIÓN 2 — PUNTOS MUESTRA
        # ---------------------------------------------------------

        self.play(
            FadeOut(partition_text),
            FadeOut(dx_arrow),
            FadeOut(dx_label)
        )

        sample_intro = Text(
            "Elegimos el punto medio de cada subintervalo.",
            font_size=21
        )

        sample_intro.move_to(
            RIGHT * 3.05 + UP * 1.15
        )

        self.play(Write(sample_intro))

        # Puntos muestra sobre el eje x
        sample_axis_dots = VGroup()
        sample_axis_labels = VGroup()

        sample_tex = [
            r"\frac14",
            r"\frac34",
            r"\frac54",
            r"\frac74"
        ]

        for x, tex in zip(samples, sample_tex):

            dot = Dot(
                axes.c2p(x, 0),
                radius=0.055,
                color=GREEN
            )

            label = MathTex(
                tex,
                font_size=20,
                color=GREEN
            )

            label.next_to(
                dot,
                DOWN,
                buff=0.12
            )

            sample_axis_dots.add(dot)
            sample_axis_labels.add(label)

        self.play(
            LaggedStart(
                *[
                    FadeIn(dot)
                    for dot in sample_axis_dots
                ],
                lag_ratio=0.2
            ),
            LaggedStart(
                *[
                    Write(label)
                    for label in sample_axis_labels
                ],
                lag_ratio=0.2
            )
        )

        self.wait(2)

        # ---------------------------------------------------------
        # DESTACAR TERCER PUNTO MUESTRA
        # ---------------------------------------------------------

        selected_axis_dot = sample_axis_dots[sample_index]

        self.play(
            selected_axis_dot.animate.scale(1.6)
        )

        sample_label = MathTex(
            r"x_3^*=\frac54",
            font_size=28,
            color=GREEN
        )

        sample_label.move_to(
            RIGHT * 3.05 + UP * 0.45
        )

        vertical_sample_line = DashedLine(
            axes.c2p(sample_x, 0),
            axes.c2p(
                sample_x,
                f(sample_x)
            ),
            color=GREEN,
            dash_length=0.06
        )

        curve_dot = Dot(
            axes.c2p(
                sample_x,
                f(sample_x)
            ),
            color=GREEN,
            radius=0.07
        )

        curve_dot.set_z_index(7)

        self.play(
            Write(sample_label),
            Create(vertical_sample_line),
            FadeIn(curve_dot)
        )

        self.wait(2)

        # ---------------------------------------------------------
        # FUNCIÓN PARA CREAR RECTÁNGULOS DE PUNTO MEDIO
        # ---------------------------------------------------------

        def midpoint_rectangles(
            number_of_rectangles,
            opacity=0.30,
            stroke_width=1.5
        ):

            delta = (b - a) / number_of_rectangles

            group = VGroup()

            for i in range(number_of_rectangles):

                left = a + i * delta
                right = left + delta

                x_star = left + delta / 2

                height = f(x_star)

                rectangle = Polygon(
                    axes.c2p(left, 0),
                    axes.c2p(right, 0),
                    axes.c2p(right, height),
                    axes.c2p(left, height),
                    fill_color=YELLOW,
                    fill_opacity=opacity,
                    stroke_color=YELLOW,
                    stroke_width=stroke_width
                )

                rectangle.set_z_index(2)

                group.add(rectangle)

            return group

        rectangles_4 = midpoint_rectangles(4)

        selected_rect = rectangles_4[sample_index]

        self.play(FadeIn(selected_rect))

        self.wait(2)

        # ---------------------------------------------------------
        # ALTURA DEL TERCER RECTÁNGULO
        # ---------------------------------------------------------

        height_formula = MathTex(
            r"f(x_3^*)"
            r"="
            r"f\left(\frac54\right)"
            r"="
            r"\left(\frac54\right)^2"
            r"="
            r"\frac{25}{16}",
            font_size=22,
            color=GREEN
        )

        height_formula.move_to(
            RIGHT * 3.05 + DOWN * 0.20
        )

        self.play(Write(height_formula))

        self.wait(3)

        # ---------------------------------------------------------
        # ÁREA DEL TERCER RECTÁNGULO
        # ---------------------------------------------------------

        contribution = VGroup(
            Text(
                "Área = base × altura",
                font_size=20
            ),
            MathTex(
                r"A_3="
                r"f(x_3^*)\Delta x"
                r"="
                r"\frac{25}{16}"
                r"\cdot"
                r"\frac12"
                r"="
                r"\frac{25}{32}",
                font_size=22
            )
        ).arrange(
            DOWN,
            buff=0.18
        )

        contribution.move_to(
            RIGHT * 3.05 + DOWN * 1.05
        )

        self.play(
            Write(contribution[0]),
            Write(contribution[1])
        )

        self.wait(3)

        # ---------------------------------------------------------
        # MOSTRAR TODOS LOS RECTÁNGULOS
        # ---------------------------------------------------------

        self.play(
            FadeOut(sample_intro),
            FadeOut(sample_label),
            FadeOut(height_formula),
            FadeOut(contribution),
            FadeOut(vertical_sample_line),
            FadeOut(curve_dot)
        )

        for index, rectangle in enumerate(rectangles_4):
            if index != sample_index:
                self.play(
                    FadeIn(rectangle),
                    run_time=0.4
                )

        self.wait(2)

        # ---------------------------------------------------------
        # SECCIÓN 3 — SUMA DE RIEMANN
        # ---------------------------------------------------------

        heights = MathTex(
            r"f(x_i^*)="
            r"\left\{"
            r"\frac1{16},"
            r"\frac9{16},"
            r"\frac{25}{16},"
            r"\frac{49}{16}"
            r"\right\}",
            font_size=21
        )

        heights.move_to(
            RIGHT * 3.05 + UP * 0.95
        )

        self.play(Write(heights))

        self.wait(2)

        sum_formula = VGroup(
            MathTex(
                r"S_4="
                r"\sum_{i=1}^{4}"
                r"f(x_i^*)\Delta x",
                font_size=25
            ),
            MathTex(
                r"="
                r"\frac{1+9+25+49}{32}",
                font_size=24
            ),
            MathTex(
                r"="
                r"\frac{21}{8}"
                r"="
                r"2.625",
                font_size=25
            )
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.20
        )

        sum_formula.move_to(
            RIGHT * 3.05 + DOWN * 0.45
        )

        for line in sum_formula:
            self.play(
                Write(line),
                run_time=0.8
            )

        self.wait(3)

        # ---------------------------------------------------------
        # COMPARACIÓN CON EL ÁREA EXACTA
        # ---------------------------------------------------------

        exact_area = VGroup(
            Text(
                "Área exacta:",
                font_size=20
            ),
            MathTex(
                r"\int_0^2 x^2\,dx"
                r"="
                r"\frac83"
                r"\approx"
                r"2.667",
                font_size=24
            )
        ).arrange(
            DOWN,
            buff=0.15
        )

        exact_area.next_to(
            sum_formula,
            DOWN,
            buff=0.40,
            aligned_edge=LEFT
        )

        self.play(
            Write(exact_area[0]),
            Write(exact_area[1])
        )

        self.wait(3)

        # ---------------------------------------------------------
        # REFINAMIENTO DE LA PARTICIÓN
        # ---------------------------------------------------------

        self.play(
            FadeOut(heights),
            FadeOut(sum_formula),
            FadeOut(exact_area),
            FadeOut(sample_axis_labels),
            FadeOut(sample_axis_dots),
            FadeOut(partition_lines)
        )

        refinement_title = Text(
            "Refinamos la partición",
            font_size=23
        )

        refinement_title.move_to(
            RIGHT * 3.05 + UP * 1.05
        )

        refinement_formula = MathTex(
            r"\Delta x=\frac{2}{n}",
            font_size=27
        )

        refinement_formula.move_to(
            RIGHT * 3.05 + UP * 0.45
        )

        n_label = MathTex(
            r"n=4",
            font_size=32,
            color=YELLOW
        )

        n_label.move_to(
            RIGHT * 3.05 + DOWN * 0.15
        )

        self.play(
            Write(refinement_title),
            Write(refinement_formula),
            Write(n_label)
        )

        self.wait(2)

        # Rectángulos actuales
        current_rectangles = rectangles_4

        # ---------------------------------------------------------
        # n = 8
        # ---------------------------------------------------------

        rectangles_8 = midpoint_rectangles(
            8,
            opacity=0.28,
            stroke_width=1.2
        )

        n_8 = MathTex(
            r"n=8",
            font_size=32,
            color=YELLOW
        ).move_to(n_label)

        self.play(
            ReplacementTransform(
                current_rectangles,
                rectangles_8
            ),
            Transform(n_label, n_8),
            run_time=1.4
        )

        current_rectangles = rectangles_8

        self.wait(2)

        # ---------------------------------------------------------
        # n = 16
        # ---------------------------------------------------------

        rectangles_16 = midpoint_rectangles(
            16,
            opacity=0.26,
            stroke_width=1
        )

        n_16 = MathTex(
            r"n=16",
            font_size=32,
            color=YELLOW
        ).move_to(n_label)

        self.play(
            ReplacementTransform(
                current_rectangles,
                rectangles_16
            ),
            Transform(n_label, n_16),
            run_time=1.4
        )

        current_rectangles = rectangles_16

        self.wait(2)

        # ---------------------------------------------------------
        # n = 32
        # ---------------------------------------------------------

        rectangles_32 = midpoint_rectangles(
            32,
            opacity=0.24,
            stroke_width=0.8
        )

        n_32 = MathTex(
            r"n=32",
            font_size=32,
            color=YELLOW
        ).move_to(n_label)

        self.play(
            ReplacementTransform(
                current_rectangles,
                rectangles_32
            ),
            Transform(n_label, n_32),
            run_time=1.4
        )

        current_rectangles = rectangles_32

        self.wait(3)

        # ---------------------------------------------------------
        # n → infinito y Δx → 0
        # ---------------------------------------------------------

        limit_description = MathTex(
            r"n\to\infty"
            r"\qquad"
            r"\Delta x\to0",
            font_size=27
        )

        limit_description.move_to(
            RIGHT * 3.05 + DOWN * 0.85
        )

        self.play(Write(limit_description))

        self.wait(3)

        # ---------------------------------------------------------
        # INTEGRAL DEFINIDA
        # ---------------------------------------------------------

        self.play(
            FadeOut(refinement_title),
            FadeOut(refinement_formula),
            FadeOut(n_label),
            FadeOut(limit_description)
        )

        connection = Text(
            "suma  →  límite  →  integral",
            font_size=23
        )

        connection.move_to(
            RIGHT * 3.05 + UP * 0.75
        )

        limit_formula = MathTex(
            r"\lim_{n\to\infty}"
            r"\sum_{i=1}^{n}"
            r"f(x_i^*)\Delta x"
            r"="
            r"\int_0^2 x^2\,dx"
            r"="
            r"\frac83",
            font_size=22
        )

        limit_formula.move_to(
            RIGHT * 3.05 + DOWN * 0.10
        )

        self.play(Write(connection))
        self.play(Write(limit_formula))

        self.wait(4)

        # ---------------------------------------------------------
        # CIERRE
        # ---------------------------------------------------------

        final_message = VGroup(
            Text(
                "Dividir",
                font_size=21
            ),
            Text(
                "Elegir puntos muestra",
                font_size=21
            ),
            Text(
                "Construir rectángulos",
                font_size=21
            ),
            Text(
                "Sumar sus áreas",
                font_size=21
            )
        ).arrange(
            DOWN,
            buff=0.12
        )

        final_message.move_to(
            RIGHT * 3.05 + DOWN * 1.30
        )

        self.play(
            FadeOut(connection),
            FadeOut(limit_formula),
            FadeIn(final_message)
        )

        self.wait(4)