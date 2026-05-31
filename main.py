import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex

class SetupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        title = Label(
            text="Paste Mark Scheme Text Below:", 
            font_size='22sp', 
            size_hint_y=None, 
            height=50,
            bold=True
        )
        layout.add(title)
        
        self.text_input = TextInput(
            text="1  A\n2  B\n3  C\n\n(Or paste content copied directly from your CIE PDF)",
            font_size='16sp',
            multiline=True,
            background_color=(0.95, 0.95, 0.95, 1)
        )
        layout.add(self.text_input)
        
        btn_parse = Button(
            text="Extract & Start Checker",
            font_size='20sp',
            size_hint_y=None,
            height=70,
            background_color=get_color_from_hex("#4CAF50"),
            background_normal=""
        )
        btn_parse.bind(on_press=self.parse_text)
        layout.add(btn_parse)
        
        self.add_widget(layout)

    def parse_text(self, instance):
        raw_text = self.text_input.text.upper()
        
        # Regex targeting numbers 1-40 paired with options A-D
        pattern = re.compile(r'\b([1-9]|[123]\d|40)\s+([A-D])(?:\s+|$)')
        matches = pattern.findall(raw_text)
        
        answer_key = {}
        for num, ans in matches:
            q_num = int(num)
            if 1 <= q_num <= 40:
                answer_key[q_num] = ans
                
        if not answer_key:
            self.text_input.text = "ERROR: No valid answers found! Check layout format."
            return
            
        checker_screen = self.manager.get_screen('checker')
        checker_screen.build_grid(answer_key)
        self.manager.current = 'checker'

class CheckerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.add_widget(self.main_layout)

    def build_grid(self, answer_key):
        self.main_layout.clear_widgets()
        self.answer_key = answer_key
        self.user_selections = {}
        self.button_rows = {} 

        # Navigation Top Bar
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=20)
        
        self.score_lbl = Label(text="Score: 0 / 40", font_size='22sp', bold=True, halign='left', valign='middle')
        self.score_lbl.bind(size=self.score_lbl.setter('text_size'))
        
        btn_reset = Button(
            text="Reset & New MS",
            size_hint_x=None,
            width=200,
            background_color=get_color_from_hex("#f44336"),
            background_normal="",
            font_size='16sp',
            bold=True
        )
        btn_reset.bind(on_press=self.go_back)
        
        top_bar.add_widget(self.score_lbl)
        top_bar.add_widget(btn_reset)
        self.main_layout.add_widget(top_bar)

        # Scrolling framework
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=15, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        # Generating Grid Items
        for i in range(1, 41):
            if i not in self.answer_key:
                continue
                
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=10)
            
            q_lbl = Label(text=f"Q{i}:", font_size='18sp', bold=True, size_hint_x=None, width=70)
            row.add_widget(q_lbl)
            
            row_buttons = {}
            for option in ['A', 'B', 'C', 'D']:
                btn = Button(
                    text=option,
                    font_size='18sp',
                    background_color=get_color_from_hex("#757575"),
                    background_normal=""
                )
                # FIX: Clean double-lambda mapping to circumvent the Kivy argument mutation bug
                btn.bind(on_press=lambda instance, q=i, opt=option: self.check_answer(q, opt))
                row.add_widget(btn)
                row_buttons[option] = btn
                
            self.button_rows[i] = row_buttons
            grid.add_widget(row)

        scroll.add_widget(grid)
        self.main_layout.add_widget(scroll)

    def check_answer(self, q_num, selected_letter):
        correct_letter = self.answer_key.get(q_num)
        self.user_selections[q_num] = selected_letter
        
        # UI cleanup loop per tap
        for letter, btn in self.button_rows[q_num].items():
            btn.background_color = get_color_from_hex("#757575")
            
        # UI Status color mapping
        if selected_letter == correct_letter:
            self.button_rows[q_num][selected_letter].background_color = get_color_from_hex("#4CAF50")
        else:
            self.button_rows[q_num][selected_letter].background_color = get_color_from_hex("#f44336")
            self.button_rows[q_num][correct_letter].background_color = get_color_from_hex("#4CAF50")

        # Score recalculation engine
        final_score = 0
        for q, ans in self.user_selections.items():
            if self.answer_key.get(q) == ans:
                final_score += 1
                
        self.score_lbl.text = f"Score: {final_score} / {len(self.answer_key)}"

    def go_back(self, instance):
        self.manager.current = 'setup'

class MCQCheckerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SetupScreen(name='setup'))
        sm.add_widget(CheckerScreen(name='checker'))
        return sm

if __name__ == '__main__':
    MCQCheckerApp().run()
