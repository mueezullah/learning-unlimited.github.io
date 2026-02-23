---
layout: default
title: Give to Learning Unlimited
---

# Give to LU

*Help each student to find their passion.*

<!-- Slideshow content -->
<div id="slideshow">
  <div class="active">
    <img src="/media/images/photos/DSC_0002.jpg" alt="Slideshow Image 1" />
    Stanford Splash students relaxing on the Stanford Quad (2009)
  </div>
  <div>
    <img src="/media/images/photos/giant_origami.jpg" alt="Slideshow Image 3" />
    Stanford Splash students folding giant origami statues (2009)
  </div>
  <div>
    <img src="/media/images/photos/Dance-Photo.jpg" alt="Slideshow Image 6" />
    Duke Splash students learning dance (2010)
  </div>
</div>

<center>
  <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=53TD5UYZ9LVXY&source=url">
    <img src="/media/images/content-pages/donate3-small.gif" alt="Donate!" border="0" />
  </a>
</center>

Learning Unlimited helps college students teach middle and high school students about everything from Machine Vision to Urban Planning to Modern Poetry—classes where students explore new material and discover their passions. We are a young nonprofit already reaching over 5,000 high school and middle school students annually through hundreds of college student volunteer teachers and leaders.

You know what it means for a teenager to find something they're passionate to learn: it's the key to discovering a lifetime of learning. With our **Splash** model, students everywhere can experience this change. Your donation helps start programs that will last for decades at universities across the nation. All donations go towards supporting the infrastructure that Splash needs: the website system, mentoring and teacher training, and shared resources that help the programs run so smoothly.

[Click here](/donatenow) to donate now by credit/debit card.

For more information, please see our [annual report](/media/docs/annualreport2011.pdf).

All donations are tax-deductible and a tax receipt will be provided to you. If you are considering a major contribution, please [contact us](/contact).

<center>
  <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=53TD5UYZ9LVXY&source=url">
    <img src="/media/images/content-pages/donate3-small.gif" alt="Donate!" border="0" />
  </a>
</center>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js"></script>
<script type="text/javascript">
function slideSwitch() {
    var $active = $('#slideshow DIV.active');

    if ( $active.length == 0 ) $active = $('#slideshow DIV:last');

    var $next =  $active.next().length ? $active.next()
        : $('#slideshow DIV:first');

    $active.addClass('last-active');

    $next.css({opacity: 0.0})
        .addClass('active')
        .animate({opacity: 1.0}, 1000, function() {
            $active.removeClass('active last-active');
        });
}

$(function() {
    setInterval( "slideSwitch()", 5000 );
});
</script>

<style type="text/css">
#slideshow {
    margin-top: 1em;
    position:relative;
    height:500px;
}

#slideshow DIV {
    position:absolute;
    top:0;
    left:0;
    z-index:8;
    opacity:0.0;
    height: 500px;
    background-color: #FFF;
    font-size: 90%;
    font-style: italic;
}

#slideshow DIV.active {
    z-index:10;
    opacity:1.0;
}

#slideshow DIV.last-active {
    z-index:9;
}

#slideshow DIV IMG {
    height: 460px;
    display: block;
    border: 0;
    margin-bottom: 10px;
}
</style>
