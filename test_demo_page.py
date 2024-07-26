from seleniumbase import BaseCase

class TestDemoPage(BaseCase):
    def test_input_slider(self):
        self.open("https://seleniumbase.io/demo_page")

         # Define the slider element
        slider = "#mySlider"
        progress_bar = "#progressBar"
        
        # Get the current value of the slider (for verification)
        initial_value = self.get_attribute(slider, "value")
        print(f"Initial slider value: {initial_value}")
        
        # Set the slider to a new value (for example, 70)
        new_value = 70
        self.set_value(slider, new_value)
        
        # Verify the slider value has been updated
        updated_value = self.get_attribute(slider, "value")
        print(f"Updated slider value: {updated_value}")
        
        # Assert the slider value to ensure the test passes
        self.assert_equal(updated_value, str(new_value))

        self.assert_attribute(progress_bar, 'value', '70')

    def test_dropdown(self):
        self.open("https://seleniumbase.io/demo_page")

         # Define the dropdown element
        dropdown = "#mySelect"
        meter_bar = "#meterBar"
        
        # Get the current value of the dropdown (for verification)
        initial_value = self.get_attribute(dropdown, "value")
        print(f"Initial dropdown value: {initial_value}")
        
        # Set the dropdown to a new value (for example, %75)
        self.select_option_by_value(dropdown, '75%')
        
        
        # Verify the dropdown value has been updated
        updated_text = self.get_attribute(dropdown, "value")
        print(f"Updated dropdown value: {updated_text}")
        
        # Assert the dropdown value to ensure the test passes
     
        self.assert_attribute(meter_bar, 'value', '0.75')
    
    def test_checkbox(self):
        self.open("https://seleniumbase.io/demo_page")

        self.assert_element_not_visible('#drop1')
        self.check_if_unchecked('#checkBox1')
        self.assert_true(self.is_selected('#checkBox1'))
        self.assert_element_visible('#drop1')

    def test_iframe(self):
        self.open("https://seleniumbase.io/demo_page")

        self.assert_element_not_visible('h4')

        self.switch_to_frame('#myFrame2')
        self.assert_text('iFrame Text', 'h4')

        self.assert_element('h4')
        self.switch_to_default_content()

        self.assert_element('#progressBar')

    def test_checkboxIniframe(self):
        self.open("https://seleniumbase.io/demo_page")

        self.assert_element_not_visible('#checkBox6')

        self.switch_to_frame('#myFrame3')
        #self.wait(3)

        self.check_if_unchecked('#checkBox6')

        #self.wait(3)

        self.assert_true(self.is_checked('#checkBox6'))

        self.switch_to_default_content()

        self.assert_element_visible('#progressBar')
    
    def test_hoverDrop(self):
        self.open("https://seleniumbase.io/demo_page")

        self.hover_and_click('#myDropdown', '#dropOption2')
        #self.hover('#myDropdown')

        #self.click('#dropOption2')

        self.assert_text('Link Two Selected', '#tbodyId h3')

        self.wait(3)
