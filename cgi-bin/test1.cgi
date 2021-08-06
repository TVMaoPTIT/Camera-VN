#!/usr/bin/perl

my $sendmail = "/usr/sbin/sendmail -t";
my $reply_to = "Reply-to: foo\@bar.org\n";
my $subject  = "Subject: Confirmation of your submission\n";
my $content  = "Thanks for your submission.";
my $file     = "subscribers.txt";

unless ($to) {
  print $query->header;
  print "Please fill in your email and try again";
}
my $LOG = "log.dat";
open (FILE, ">>$LOG") or die "Cannot open $LOG: $!";
print FILE ,"JBB";
close(FILE); 

my $send_to  = "To: jaybrianb\@yahoo.com");

open(SENDMAIL, "|$sendmail") or die "Cannot open $sendmail: $!";
print SENDMAIL $reply_to;
print SENDMAIL $subject;
print SENDMAIL $send_to;
print SENDMAIL "Content-type: text/plain\n\n";
print SENDMAIL $content;
close(SENDMAIL);

print "Content-type: text/html\n\n";
print "<html>\n\n";
print "<head><title>test</title></head>\n";
print "<body>\n";
print "you did something\n";
print "</body>\n";
print "</html>";
© 2021 GitHub, Inc.
