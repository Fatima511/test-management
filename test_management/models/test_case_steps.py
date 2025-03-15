from odoo import models, fields

class TestCaseSteps(models.Model):
    """
    Model representing the steps of a test case.


    """
    _name = 'test.case.steps'
    _description = 'Test Case steps model'

    num = fields.Integer(string="#", required=True, default=1)
    action = fields.Char(string="Action", required=True)
    expected_result = fields.Text(string="Expected Result")
    test_case_id = fields.Many2one('test.case')


class TestRunSteps(models.Model):
    """
    Model representing the steps of a test run.

    """
    _name = 'test.run.steps'
    _description = 'Test run steps model'

    num = fields.Integer(string="#", required=True)
    action = fields.Char(string="Action", required=True)
    expected_result = fields.Text(string="Expected Result")
    actual_result = fields.Text(string="Actual Result")
    test_case_id = fields.Many2one('test.case')
    test_run_id = fields.Many2one('test.run')
    result = fields.Selection(
        selection=[
            ('failed', 'Failed'),
            ('passed', 'Passed'),
            ('blocked', 'Blocked'),
        ],
        string='Result',
    )

    def passed(self):
        """
        Marks the test step as passed.
        If no actual result is provided, it defaults to "As it is expected!".
        """
        if not self.actual_result:
            self.actual_result = "As it is expected!"
        self.result = 'passed'

    def failed(self):
        """Marks the test step as failed."""
        self.result = 'failed'

    def blocked(self):
        """Marks the test step as blocked."""
        self.result = 'blocked'

    def report_bug(self):
        """
        Opens a bug creation form with pre-filled data from the test run steps.

        Returns:
            dict: Action dictionary to open the bug creation form.
        """
        self.ensure_one()

        # Search for related test steps
        test_steps = self.env['test.run.steps'].search([
            ('test_case_id', '=', self.test_case_id.id),
            ('test_run_id', '=', self.test_run_id.id)
        ])

        # Prepare description for the bug
        description_lines = []
        for line in test_steps:
            description_lines.append(f"Step: {line.action}")
            description_lines.append(f"Expected Result: {line.expected_result}")
            description_lines.append(f"Actual Result: {line.actual_result}")
            description_lines.append(f"Result: {line.result}")
            description_lines.append("")  # Blank line for readability

        # Join all lines into a single string
        concatenated_values = "\n".join(description_lines)

        # Return action to open the bug creation form
        return {
            'name': 'Bug',
            'type': 'ir.actions.act_window',
            'res_model': 'test.bug',
            'view_mode': 'form',
            'context': {
                'default_test_case_id': self.test_case_id.id,
                'default_description': concatenated_values,
                'default_test_run_id': self.test_run_id.id,
                'default_name': self.test_case_id.name + " Bug",
                'force_save': True,
            },
            'target': 'new',
        }
