#!/usr/bin/python3
# 
# Generate Invoice Script
# 
# Description: A small python script designed to print out HTML invoices.
# 

# Necessary imports
import time
from pycss import generate_stylesheet

# Global definitions for the Company sending the invoice.
doc_title              = "Customer Invoice"
company_logo_img       = "invoice_logo.png"
company_name           = "XYZ Corporation"
company_street_address = "456 Generic Lane"
company_state_country  = "City, State, Country"
company_email          = "email@address.xyz"
company_phone          = "000-000-0000"

# Global definitions for the Client receiving the invoice.
client_name            = "John Smith"
client_street_address  = "123 Fake Street"
client_state_country   = "City, State, Country"
client_postal          = "ABC 123"
client_account         = "00000000000"

# Global definitions for the current order being processed.
order_date             = "June 1, 2017"
order_method           = "Electronic Deposit"

# Global list of goods or services being purchased; defined as follows:
#
# 1) Description
# 2) Hours
# 3) Hourly rate in dollars
#
order_details_array = [
  ["Sample Order Name", 7, 75]
]

# Current Taxable Rate, as a percent.
taxable_rate = 0.12

# Global definition for the invoice-specific notes.
notes  = "" 
notes += "Your request has been delivered as-is electronically. " 
notes += "For more information regarding this or other orders, " 
notes += "consider contacting XYZ Corporation via email " 
notes += "at email@address.xyz or by phone at " 
notes += "000-000-0000 for order assistance." 

# Global defintion of the final thank you
thank_you  = ""
thank_you += "Thank you for choosing XYZ Corporation, we look " 
thank_you += "forward to working with you again." 

#
# Function to generate the specific order number.
#
def generate_order_number():

    # Attempt to grab the current epoch time.
    tmp_num = str(time.time())
    if (len(tmp_num) < 1):
        return ""

    # Since the time call returns possible milliseconds, then split the result.
    parts = tmp_num.split(".")

    # If the second element is blank, add two zeros.
    if (len(parts[1]) == 0):
        return parts[0] + "00"

    # If the second element is only one digit, add an extra zero.
    if (len(parts[1]) == 1):
        return parts[0] + "" + parts[1] + "0"
    
    # If the second element is two digits, append the two parts together.
    if (len(parts[1]) == 2):
        return parts[0] + parts[1]

    # In the event something really odd occurred, which it shouldn't, force
    # the program to ignore the second part.
    return parts[0] + "00"

#
# Function to assemble the <head> section of the document.
#
def assemble_head_section(document_title):

    head_html = ""

    head_html += "    <!-- Head -->\n" 
    head_html += "    <head>\n" 
    head_html += "        <meta charset=\"utf-8\" />\n" 
    head_html += "        <meta name=\"description\" content=\"Customer Invoice\" />\n" 
    head_html += "        <meta name=\"keywords\" content=\"invoice template\" />\n"
    head_html += "        <meta name=\"robots\" content=\"index,follow\" />\n" 
    head_html += "        <meta name=\"author\" content=\"John Smith\" />\n" 
    head_html += generate_stylesheet()
    head_html += "        <title>" + document_title + "</title>\n" 
    head_html += "    </head>\n"

    return head_html

#
# Function to assemble the header section of the invoice.
#
def assemble_invoice_header_section(logo_img, name, street_address, email, state_country, phone):

    header_section_html  = ""

    header_section_html += "             <!-- Document Header -->\n" 
    header_section_html += "             <div id=\"invoice_header\">\n" 
    header_section_html += "                 <div id=\"invoice_image_area\">\n"
    header_section_html += "                     <img id=\"logo\" src=\"" + logo_img + "\" alt=\"" + name + "\" />\n"
    header_section_html += "                 </div>\n"
    header_section_html += "                 <div id=\"invoice_text_area\">\n"
    header_section_html += "                     <div id=\"company_name\">\n" 
    header_section_html += "                     " + name + "\n"
    header_section_html += "                     </div>\n" 
    header_section_html += "                     <table id=\"company_details\">\n"
    header_section_html += "                         <tr>\n"
    header_section_html += "                             <td>\n"
    header_section_html += "                               " + street_address + "\n"
    header_section_html += "                             </td>\n"
    header_section_html += "                             <td>\n"
    header_section_html += "                               " + email + "\n"
    header_section_html += "                             </td>\n" 
    header_section_html += "                         </tr>\n" 
    header_section_html += "                         <tr>\n" 
    header_section_html += "                             <td>\n" 
    header_section_html += "                               " + state_country + "\n" 
    header_section_html += "                             </td>\n" 
    header_section_html += "                             <td>\n" 
    header_section_html += "                               " + phone + "\n"
    header_section_html += "                             </td>\n"
    header_section_html += "                         </tr>\n"
    header_section_html += "                     </table>\n"
    header_section_html += "                 </div>\n"
    header_section_html += "             </div>\n"

    return header_section_html

#
# Function to assemble the client information section of the invoice.
#
def assemble_invoice_client_information_section(name, street_address, state_country, postal, account):

    client_section_html  = ""

    client_section_html += "                 <!-- Customer Information -->\n"
    client_section_html += "                 <div id=\"customer_info\">\n"
    client_section_html += "                     <table>\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <th>\n"
    client_section_html += "                               Customer Information\n" 
    client_section_html += "                             </th>\n" 
    client_section_html += "                             <th>\n"
    client_section_html += "                             </th>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- Buffer -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "                         </tr>\n"
   
    client_section_html += "                         <!-- Client Name -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>Name:</td>\n"
    client_section_html += "                             <td>" + name + "</td>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- Street Address -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>Address:</td>\n"
    client_section_html += "                             <td>" + street_address + "</td>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- City, Province/State, Country -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "			     <td>" + state_country + "</td>\n"
    client_section_html += "                         </tr>\n"
   
    client_section_html += "                         <!-- Postal Code -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "			     <td>" + postal + "</td>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- Account Number is just a number -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>Account Number:</td>\n"
    client_section_html += "			      <td>" + account + "</td>\n"
    client_section_html += "                         </tr>\n"
    client_section_html += "                     </table>\n"
    client_section_html += "                 </div>\n"

    return client_section_html

#
# Function to assemble the order information section of the invoice.
#
def assemble_invoice_order_information_section(number, date, method):

    order_info_section_html = ""
 
    order_info_section_html += "                 <!-- Order Information -->\n"
    order_info_section_html += "                 <div id=\"order_info\">\n"
    order_info_section_html += "                     <table>\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <th>\n"
    order_info_section_html += "                               Order Information\n"
    order_info_section_html += "                             </th>\n"
    order_info_section_html += "                             <th>&nbsp;</th>\n"
    order_info_section_html += "                         </tr>\n" 
    
    order_info_section_html += "                         <!-- Buffer -->\n"
    order_info_section_html += "                         <tr>\n" 
    order_info_section_html += "                             <td>&nbsp;</td>\n"
    order_info_section_html += "                             <td>&nbsp;</td>\n"
    order_info_section_html += "                         </tr>\n"
    
    order_info_section_html += "                         <!-- Order Number is timestamp -->\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <td>Number:</td>\n"
    order_info_section_html += "                             <td>" + str(number) + "</td>\n"
    order_info_section_html += "                         </tr>\n"
    
    order_info_section_html += "                         <!-- Order Date -->\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <td>Date:</td>\n"
    order_info_section_html += "                             <td>" + date + "</td>\n"
    order_info_section_html += "                         </tr>\n"
    
    order_info_section_html += "                         <!-- Order Payment Method -->\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <td>Method:</td>\n"
    order_info_section_html += "                             <td>" + method + "</td>\n"
    order_info_section_html += "                         </tr>\n"
    order_info_section_html += "                     </table>\n"
    order_info_section_html += "                 </div>\n"

    return order_info_section_html

#
# Function to assemble the order details section of the invoice.
#
def assemble_invoice_order_details_section(details_array, taxable_rate):

    num_of_orders              = len(details_array)
    current_num                = 0
    current_type               = "odd"
    order_details_section_html = ""
    invoice_cost_summary       = 0

    order_details_section_html += "                 <!-- Main Table of Supplied Goods and Services -->\n"
    order_details_section_html += "                 <table id=\"order_details_table\">\n"
    order_details_section_html += "                     <tr>\n"
    order_details_section_html += "                         <th class=\"requested_service_column\">\n"
    order_details_section_html += "                             Requested Service\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"hours_column\">\n"
    order_details_section_html += "                             Hours\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"hour_rate_column\">\n"
    order_details_section_html += "                             Hourly Rate\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"cost_column\">\n"
    order_details_section_html += "                             Amount\n"
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                     </tr>\n" 
    order_details_section_html += "                     <tr class=\"odd\">\n"
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                     </tr>\n" 
   
    # Generate the HTML table tags for each of the orders.
    for current_num in range (0, num_of_orders):
 
        # Sanity check, ensure this is an actual entry, otherwise skip
        if (details_array[current_num] is None):
            continue

        # Sanity check, make sure we got a proper entry, else skip to the next
        if (len(details_array[current_num]) != 3):
            continue

        # Stagger the <tr> css styles to produce a line-by-line effect
        if (current_type == "odd"):
            current_type = "even"
        else:
            current_type = "odd"
        
        # Calculate the cost of a given service.
        cost = details_array[current_num][1] * details_array[current_num][2]
        invoice_cost_summary += cost

        # Format the hourly rate / entry cost.
        hourly_rate = "{:.2f}".format(details_array[current_num][2])
        cost = "{:.2f}".format(cost)

        # Generate the <tr> and <td> elements based on the current entry.
        order_details_section_html += "                     <tr class=\"" + current_type + "\">\n"
        order_details_section_html += "                         <td>" + details_array[current_num][0] + "</td>\n"
        order_details_section_html += "                         <td>" + str(details_array[current_num][1]) + "</td>\n"
        order_details_section_html += "                         <td>$" + hourly_rate + " / hour</td>\n"
        order_details_section_html += "                         <td class=\"align_dollars\">$" + cost + "</td>\n"
        order_details_section_html += "                     </tr>\n"
    
    # Generate the HTML <tr> buffers to make the page standard height.
    if (num_of_orders < 7):

        # Go ahead and cycle based on how much more space we need. 
        for x in range (0, 7 - num_of_orders):

            # Stagger the <tr> css styles to produce a line-by-line effect
            if (current_type == "odd"):
                current_type = "even"
            else:
                current_type = "odd"

            # Append the necessary buffer rows to the table.
            order_details_section_html += "                     <!-- Buffer Rows -->\n"
            order_details_section_html += "                     <tr class=\"" + current_type + "\">\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                     </tr>\n" 
    
    # If the previous entry was "even" make sure we have an "odd" separator
    # to improve page appearance.
    if (current_type == "even"):
        order_details_section_html += "                     <!-- Buffer Separator -->\n"
        order_details_section_html += "                     <tr class=\"odd\">\n"
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                     </tr>\n"

    order_details_section_html += "                     <!-- Cost Summary Before Tax -->\n"
    order_details_section_html += "                     <tr class=\"odd\">\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n" 
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                         <th>\n" 
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                            Summary\n"
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                         <th class=\"align_dollars\">\n" 
    order_details_section_html += "                            $"
    order_details_section_html += ("{:.2f}".format(invoice_cost_summary)) + "\n" 
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                     </tr>\n"
 
    order_details_section_html += "                     <!-- Taxes -->\n"
    order_details_section_html += "                     <tr class=\"odd\">\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                            Tax\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"align_dollars\">\n"
    order_details_section_html += "                            $"
    order_details_section_html += ("{:.2f}".format(invoice_cost_summary * taxable_rate)) + "\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                     </tr>\n"
   
    order_details_section_html += "                     <!-- Total -->\n"
    order_details_section_html += "                     <tr class=\"odd\">\n" 
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                         <th>\n" 
    order_details_section_html += "                            Total\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"align_dollars\">\n"
    order_details_section_html += "                            $"
    order_details_section_html += ("{:.2f}".format(invoice_cost_summary * (1 + taxable_rate))) + "\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                     </tr>\n"
    order_details_section_html += "                 </table>\n"

    return order_details_section_html

#
# PROGRAM MAIN
#
def main():

    html = ""

    html += "<!DOCTYPE html>\n"
    html += "<html lang=\"en\">\n"
     
    html += assemble_head_section(doc_title)
 
    html += "    <body>\n"
    html += "        <div id=\"central_element\">\n"
    
    # Assemble the header of the invoice, with company logo and information.
    html += assemble_invoice_header_section(company_logo_img,
                                            company_name,
                                            company_street_address,
                                            company_email,
                                            company_state_country,
                                            company_phone)

    html += "             <hr />\n"
    
    # Assemble the customer information section.
    html += "             <!-- Customer & Order Information Section -->\n"
    html += "             <div id=\"customer_and_order_information\">\n"
   
    # Assemble the client information section of the invoice. 
    html += assemble_invoice_client_information_section(client_name,
                                                        client_street_address,
                                                        client_state_country,
                                                        client_postal,
                                                        client_account)

    # Attempt to generate an order number.
    order_number = generate_order_number()
    if (len(order_number) < 1):
        print("Error: Unable to generate order number!\n")
        return 1

    # Assemble the order information section of the invoice.
    html += assemble_invoice_order_information_section(order_number,
                                                       order_date,
                                                       order_method)

    # Close the client / order info section.
    html += "             </div>\n"
    
    html += "             <hr />\n"
    
    html += "             <!-- Order Details Section -->\n"
    html += "             <div id=\"order_details\">\n"
    html += assemble_invoice_order_details_section(order_details_array,
                                                   taxable_rate)
    html += "             </div>\n"
    
    html += "             <hr />\n"
    
    html += "             <!-- Additional message content -->\n"
    html += "             <div id=\"message_content\">\n"
    html += "                 <table>\n"
    html += "                     <tr>\n"
    html += "                         <th>Notes</th>\n"
    html += "                     </tr>\n"
    html += "                     <tr>\n"
    html += "                         <td>\n"
    html += "                           " + notes + "\n"
    html += "                         <td>\n"
    html += "                     </tr>\n"
    html += "                 </table>\n"
    html += "             </div>\n"
    
    html += "             <hr />\n"
    
    html += "             <!-- Thank you message -->\n"
    html += "             <div id=\"thank_you\">\n"
    html += "                 <strong>\n"
    html += "                   " + thank_you + "\n"
    html += "                 </strong>\n" 
    html += "             </div>\n"
    
    html += "        </div>\n"
    html += "    </body>\n"
     
    html += "</html>\n"
     
    print (html)
    return 0

######
main()
