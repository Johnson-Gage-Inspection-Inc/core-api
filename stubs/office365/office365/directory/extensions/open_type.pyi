from office365.directory.extensions.extension import Extension as Extension

class OpenTypeExtension(Extension):
    @property
    def extension_name(self) -> str | None: ...
