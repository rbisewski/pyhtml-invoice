#!/usr/bin/python
# 
# Generate CSS for HTML Invoice
# 
# Description: A simple python script designed to assemble CSS.
# 
# Author: Robert Bisewski <contact@ibiscybernetics.com>
# 

#
# Function to generate the style element contents.
#
def generate_stylesheet():

    # String to hold the css values.
    css = "    <style>\n"

    # Central element styles
    css += "    /*\n"
    css += "     * Central Element\n"
    css += "     */\n"
    css += "    #central_element {\n"
    css += "        border: solid grey 2px;\n"
    css += "        border-radius: 10px;\n"
    css += "        font-size: 12px;\n"
    css += "        margin: 30px auto;\n"
    css += "        text-align: center;\n"
    css += "        width: 800px;\n"
    css += "    }\n"
    css += "\n"

    # Header styles
    css += "    /*\n"
    css += "     * Header Styles\n"
    css += "     */\n"
    css += "    #invoice_header {\n"
    css += "        height: 160px;\n"
    css += "        width: 800px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #invoice_header #logo {\n"
    css += "        height: 65px;\n"
    css += "        width: 400px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #invoice_header #invoice_image_area {\n"
    css += "        height: 75px;\n"
    css += "        padding: 10px 10px 0px 10px;\n"
    css += "        text-align: left;\n"
    css += "        width: 800px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #invoice_header #invoice_text_area {\n"
    css += "        height: 80px;\n"
    css += "        padding: 0px 10px 10px 15px;\n"
    css += "        text-align: left;\n"
    css += "        width: 800px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #invoice_header #invoice_text_area #company_name {\n"
    css += "        padding-bottom: 15px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #invoice_header #invoice_text_area #company_details td {\n"
    css += "        width: 220px;\n"
    css += "    }\n"
    css += "\n"

    # Customer information styles
    css += "    /*\n"
    css += "     * Customer Information\n"
    css += "     */\n"
    css += "    #customer_and_order_information {\n"
    css += "        height: 125px;\n"
    css += "        padding: 10px 10px 10px 10px;\n"
    css += "        text-align: left;\n"
    css += "        width: 800px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #customer_and_order_information #customer_info {\n"
    css += "        float: left;\n"
    css += "        width: 400px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #customer_and_order_information #order_info {\n"
    css += "        float: right;\n"
    css += "        width: 400px;\n"
    css += "    }\n"
    css += "\n"

    # Order details styles
    css += "    /*\n"
    css += "     * Order Details\n"
    css += "     */\n"
    css += "    #order_details {\n"
    css += "        padding: 10px 10px 10px 10px;\n"
    css += "        text-align: left;\n"
    css += "        width: 800px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #order_details_table {\n"
    css += "        border-collapse: collapse;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #order_details_table td,\n"
    css += "    #order_details_table th {\n"
    css += "        padding: 5px;\n"
    css += "    }\n"
    css += "    \n"
    css += "    #order_details_table .requested_service_column {\n"
    css += "        width: 501px;\n"
    css += "    }\n"
    css += "    #order_details_table .hours_column {\n"
    css += "        width: 60px;\n"
    css += "    }\n"
    css += "    #order_details_table .hour_rate_column {\n"
    css += "        width: 100px;\n"
    css += "    }\n"
    css += "    #order_details_table .cost_column {\n"
    css += "        width: 80px;\n"
    css += "    }\n"
    css += "    #order_details_table .odd {\n"
    css += "        background-color: white;\n"
    css += "    }\n"
    css += "    #order_details_table .even {\n"
    css += "        background-color: #cbdaf1;\n"
    css += "    }\n"
    css += "    #order_details_table .align_dollars {\n"
    css += "        padding-right: 10px;\n"
    css += "        text-align: right;\n"
    css += "    }\n"
    css += "\n"

    # Message centre styles
    css += "    /*\n"
    css += "     * Message Centre\n"
    css += "     */\n"
    css += "    #message_content {\n"
    css += "        padding: 10px 10px 10px 10px;\n"
    css += "        text-align: left;\n"
    css += "        width: 800px;\n"
    css += "    }\n"
    css += "\n"

    # Thank you styles
    css += "    /*\n"
    css += "     * Thank You\n"
    css += "     */\n"
    css += "    #thank_you {\n"
    css += "        height: 20px;\n"
    css += "        font-style: italic;\n"
    css += "        width: 800px;\n"
    css += "    }\n"

    # End the style tag.
    css += "    </style>\n"

    # Return the completed CSS string
    return css
