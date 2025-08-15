# Link Handler Enhance

![Alpha](https://img.shields.io/badge/maturity-Alpha-red.png)
![license](https://img.shields.io/badge/licence-AGPL--3-blue.png)
[![author](https://img.shields.io/badge/Alexmalab-24292f.png?logo=github)](https://github.com/Alexmalab)
[![repo](https://img.shields.io/badge/OdooFrontendExtensions-f1f8ff.png?logo=github&logoColor=0366d6)](https://github.com/Alexmalab/OdooFrontendExtensions/tree/18.0/link_handler_enhance)

## Description

Added 2 attributes support to url link `a` tag:
- `data-oe-view-id`: specify which view id used; 
- `data-oe-action-id`: specify which action id used, now support for access action by id;

## Explanation:

If you want to send an im message within sale orders with link, you may use `_get_html_link` method:
```python
links = (
     record._get_html_link(title=record.name)
     for record in self
)
message_body = Markup("Order(s) %s need to check.") % Markup(", ".join(map(str, links)))

channel.message_post(
    author_id=...,
    body=message_body,
    message_type='comment',
    subtype_xmlid='mail.mt_comment'
)
```
Supposing you have a custom view inherited(using primary mode) by the default view of the model, for example an independent form view for sale.order,

if you are using the method above, it will always use the default form view id, specifically the default action id,

But you want the recipient open the order with specific customized view you may use this module by the following usage; 

Use `data-oe-view-id` to specify which view you want one to open this record.
```python
view_id = self.env.ref('module.view_xxx_custom_form').id
links = (
    Markup("<a href=# data-oe-model='%s' data-oe-id='%s' data-oe-view-id='%s'>%s</a>") % (
        record._name, record.id, view_id, record.name)
    for record in self
)
im_msg = Markup("You have been assigned to do your job for this order: %s") % Markup(
            ", ".join(map(str, links)))
```
## Bug Tracker
Bugs are tracked on [GitHub Issues](https://github.com/Alexmalab/OdooFrontendExtensions/issues). In case of trouble, please check there if your issue has already been reported. If you spotted it first, help us to smash it by providing a detailed and welcomed feedback.

## Credits
### Authors

- [Alexandre Ma](https://github.com/Alexmalab)

### Contributors

- Alexandre Ma<[a1exma@hotmail.com](mailto:a1exma@hotmail.com)>

### Copyright

The copyright of this module belongs to [Alexandre Ma](https://github.com/Alexmalab)

## License
   - ![license](https://img.shields.io/badge/licence-AGPL--3-blue.png)
