from django.db import models
from django.utils.translation import gettext_lazy as _


class AttachmentTypeChoices(models.TextChoices):
    IMAGE = "image", _("Image")
    VIDEO = "video", _("Video")
    AUDIO = "audio", _("Audio")
    DOCUMENT = "document", _("Document")
    OTHER = "other", _("Other")


class AttachmentMimeType(models.TextChoices):
    IMAGE_JPEG = "image/jpeg", _("JPEG")
    IMAGE_PNG = "image/png", _("PNG")
    IMAGE_GIF = "image/gif", _("GIF")
    IMAGE_SVG = "image/svg+xml", _("SVG")
    VIDEO_MP4 = "video/mp4", _("MP4")
    VIDEO_MPEG = "video/mpeg", _("MPEG")
    VIDEO_WEBM = "video/webm", _("WEBM")
    AUDIO_MP3 = "audio/mpeg", _("MP3")
    AUDIO_OGG = "audio/ogg", _("OGG")
    AUDIO_WAV = "audio/wav", _("WAV")
    APPLICATION_PDF = "application/pdf", _("PDF")
    APPLICATION_DOC = "application/msword", _("DOC")
    APPLICATION_DOCX = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        _("DOCX"),
    )
    APPLICATION_XLS = "application/vnd.ms-excel", _("XLS")
    APPLICATION_XLSX = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        _("XLSX"),
    )
    APPLICATION_PPT = "application/vnd.ms-powerpoint", _("PPT")
    APPLICATION_PPTX = (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        _("PPTX"),
    )
    TEXT_PLAIN = "text/plain", _("TXT")
    TEXT_HTML = "text/html", _("HTML")
    TEXT_XML = "text/xml", _("XML")
    TEXT_JSON = "application/json", _("JSON")
    OTHER = "other", _("Other")


class PlaceShiftChoices(models.TextChoices):
    MORNING = "morning", _("Morning")
    AFTERNOON = "afternoon", _("Afternoon")
    EVENING = "evening", _("Evening")
    NIGHT = "night", _("Night")
