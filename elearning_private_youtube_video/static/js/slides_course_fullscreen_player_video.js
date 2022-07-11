odoo.define('elearning_private_youtube_video.fullscreen', function (require) {
"use strict";

var core = require('web.core');
var QWeb = core.qweb;
var Fullscreen = require('@website_slides/js/slides_course_fullscreen_player')[Symbol.for("default")];

Fullscreen.include({
    xmlDependencies: (Fullscreen.prototype.xmlDependencies || []).concat(
        ["/elearning_private_youtube_video/static/website_slides_fullscreen.xml"]
    ),

});
});