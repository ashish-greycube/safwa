# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "safwa"
app_title = "Safwa"
app_publisher = "GreyCube Technologies"
app_description = "Item weight based on customer customization"
app_icon = "octicon octicon-check-circle"
app_color = "black"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/safwa/css/safwa.css"
# app_include_js = "/assets/safwa/js/safwa.js"

# include js, css files in header of web template
# web_include_css = "/assets/safwa/css/safwa.css"
# web_include_js = "/assets/safwa/js/safwa.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
"Sales Order" : "public/js/item_weight.js",
"Sales Invoice" : "public/js/item_weight.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "safwa.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "safwa.install.before_install"
# after_install = "safwa.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "safwa.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"validate": "safwa.selling_controller.update_customer_speicific_item_weight",
	},
	"Sales Invoice": {
		"validate": "safwa.selling_controller.update_customer_speicific_item_weight",
	}	
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"safwa.tasks.all"
# 	],
# 	"daily": [
# 		"safwa.tasks.daily"
# 	],
# 	"hourly": [
# 		"safwa.tasks.hourly"
# 	],
# 	"weekly": [
# 		"safwa.tasks.weekly"
# 	]
# 	"monthly": [
# 		"safwa.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "safwa.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "safwa.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "safwa.task.get_dashboard_data"
# }

