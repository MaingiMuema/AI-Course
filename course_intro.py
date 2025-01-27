from manim import *

class CourseIntroduction(Scene):
    def construct(self):
        # Title sequence
        title = Text("Comprehensive AI Development Course", font_size=40)
        subtitle = Text("From Foundations to Real-World Applications", font_size=30)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Course Overview
        overview = Text("Your Journey to AI Mastery", font_size=36, color=BLUE)
        overview_subtitle = Text("20-36 weeks of intensive learning", font_size=24)
        overview_subtitle.next_to(overview, DOWN)
        
        self.play(Write(overview))
        self.play(FadeIn(overview_subtitle))
        self.wait(2)
        self.play(FadeOut(overview), FadeOut(overview_subtitle))

        # Stage Details
        stages_data = [
            {
                "title": "Stage 1: AI Foundations",
                "duration": "4-6 weeks",
                "points": [
                    "• Python & Essential Math",
                    "• AI History & Types",
                    "• NumPy & Pandas",
                    "• Mini-Project: Basic Recommender"
                ]
            },
            {
                "title": "Stage 2: ML Fundamentals",
                "duration": "6-8 weeks",
                "points": [
                    "• Supervised Learning",
                    "• Unsupervised Learning",
                    "• Model Evaluation",
                    "• Project: Real-world ML"
                ]
            },
            {
                "title": "Stage 3: Deep Learning",
                "duration": "8-10 weeks",
                "points": [
                    "• Neural Networks",
                    "• CNN & RNN",
                    "• TensorFlow/PyTorch",
                    "• Project: AI Vision/NLP"
                ]
            },
            {
                "title": "Stage 4: AI Agents",
                "duration": "8-12 weeks",
                "points": [
                    "• Reinforcement Learning",
                    "• Multi-Agent Systems",
                    "• LangChain & Hugging Face",
                    "• Project: Smart Agent"
                ]
            },
            {
                "title": "Stage 5: Specialization",
                "duration": "Ongoing",
                "points": [
                    "• Generative AI & LLMs",
                    "• AI Ethics & Governance",
                    "• Production Deployment",
                    "• Capstone Project"
                ]
            }
        ]

        for i, stage in enumerate(stages_data):
            # Create stage title
            stage_title = Text(stage["title"], font_size=32, color=YELLOW)
            duration = Text(f"Duration: {stage['duration']}", font_size=24, color=BLUE)
            duration.next_to(stage_title, DOWN)

            # Create bullet points
            points = VGroup()
            for j, point in enumerate(stage["points"]):
                bullet = Text(point, font_size=24)
                if j == 0:
                    bullet.next_to(duration, DOWN*1.5)
                else:
                    bullet.next_to(points[j-1], DOWN)
                points.add(bullet)

            # Group all elements
            stage_group = VGroup(stage_title, duration, points)
            stage_group.center()

            # Animate
            self.play(Write(stage_title))
            self.play(FadeIn(duration))
            for point in points:
                self.play(Write(point), run_time=0.5)
            self.wait(2)
            self.play(FadeOut(stage_group))

        # Key Benefits
        benefits_title = Text("Why Choose This Course?", font_size=36, color=GREEN)
        self.play(Write(benefits_title))
        self.wait(1)
        
        benefits = [
            "✓ Hands-on Project Experience",
            "✓ Industry-Relevant Skills",
            "✓ Comprehensive Curriculum",
            "✓ Progressive Learning Path",
            "✓ Real-world Applications",
            "✓ Expert-designed Content"
        ]

        benefits_group = VGroup()
        for i, benefit in enumerate(benefits):
            benefit_text = Text(benefit, font_size=30)
            if i == 0:
                benefit_text.next_to(benefits_title, DOWN*2)
            else:
                benefit_text.next_to(benefits_group[-1], DOWN)
            benefits_group.add(benefit_text)
            self.play(Write(benefit_text))
        
        self.wait(2)
        self.play(FadeOut(benefits_title), FadeOut(benefits_group))

        # Final Call to Action
        cta = Text("Start Your AI Journey Today!", font_size=40, color=YELLOW)
        contact = Text("Subscribe now to always be updated.", font_size=24)
        contact.next_to(cta, DOWN)
        
        self.play(Write(cta))
        self.play(FadeIn(contact))
        self.wait(2)
