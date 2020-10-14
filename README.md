# Whatsapp_Automation
This is a beautiful script which can serve as replacement for WhatsApp Business account as you can use this
to create a bot which can be connected with a Database anywhere and fetch data from there and push that as
a message to number specified.

Basically this scripts runs continously in  background and fetches data from my firebase databse
and I have data in it like {message:"some message",number:"To be deliver to whatsapp number"} soif any action
happens in my use case where iwish to send message to my user I just push that it into db this scripts fetches it
and uses selenium to send message to  that user.

It can be very easy for you to take this script and built your own thing until our stacks are similar
Check if you are
✅Using firebase to store messages that you want to sent to someone after some action
like some people signing up for your blog and you want to use this script to tell them
about any post you push that message about the blog and ther contact in firebase.
✅Running this continosly on a cloud or maybe on your own system.
