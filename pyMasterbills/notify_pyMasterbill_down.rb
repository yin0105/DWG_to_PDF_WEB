require 'net/smtp'

message = <<MESSAGE_END
From: System Watcher <administrator@omegadesign.com>
BCC: <dkurman@omegadesign.com>, 
MIME-Version: 1.0
Content-type: text/html
Subject: pyMasterbill Process is down!

<div style="font-size: 14pt; font-family: arial;">
pyMasterbill Process is down.<br> <br> 

</div>

<i>Thanks for your help, </i><br>

MESSAGE_END

Net::SMTP.start('exchange01') do |smtp|
  smtp.send_message message, 'dkurman@omegadesign.com', 
                             'dkurman@omegadesign.com'
end

