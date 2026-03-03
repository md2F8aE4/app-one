from odoo import http
from odoo.http import request 
import io
import xlsxwriter
from ast import literal_eval





class xlsxpropertyreport(http.Controller):

    @http.route('/property/excel/report/<string:property_ids>', type='http', auth='user')
    def download_xlsx_report(self, property_ids):
        try:
            parsed_ids = literal_eval(property_ids)
        except (ValueError, SyntaxError):
            parsed_ids = []

        property_ids = request.env['property'].browse(parsed_ids)
        print(property_ids)

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()


        header_format = workbook.add_format({'bold': True, 'bg_color': "#606160", 'border': 1, 'align': 'center'})
        string_format = workbook.add_format({ 'border': 1, 'align': 'center'})
        price_format = workbook.add_format({ 'num_format': '$#,##0.00', 'border': 1, 'align': 'center'})

        headers = [' Name', 'postcode', 'selling price','garden']

        for col_num, header in enumerate(headers):
           worksheet.write(0, col_num, header, header_format)

        row_num = 1
        for property in property_ids:
            worksheet.write(row_num,0,property.name,string_format)
            worksheet.write(row_num,1,property.postcode,string_format)
            worksheet.write(row_num,2,property.selling_price, price_format)
            worksheet.write(row_num,3, 'Yes' if property.garden else 'No', string_format)

            row_num +=1
        
        

      
        workbook.close()

        
        output.seek(0)  #تقرا من بداية الملف
 
        file_name = 'property_report.xlsx'


        return request.make_response(
            output.getvalue(),
            headers=[
                ('Content-type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', f'attachment; filename="{file_name}"'),
            ]
        )
