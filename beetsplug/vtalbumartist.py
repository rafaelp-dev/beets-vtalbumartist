from beets.plugins import BeetsPlugin
from beets.importer import action
from beets import ui
from beets import mediafile

class VTAlbumArtist(BeetsPlugin):
  def __init__(self):
    super(VTAlbumArtist, self).__init__()
    
    self.albumartist = None
    self.should_set = False
    
    self.register_listener('import_task_choice', self._import_after_apply)
    self.register_listener('write', self._before_write)
    
    field = mediafile.MediaField(
        mediafile.MP3DescStorageStyle(u'VT Album Artist'),
        mediafile.MP4StorageStyle(u'----:com.apple.iTunes:VT Album Artist'),
        mediafile.ASFStorageStyle(u'VT/Album Artist'),
        mediafile.StorageStyle(u'VT_ALBUMARTIST')
    )
    self.add_media_field('vt_albumartist', field)
  
  def try_sync(self, item):
    if 'vt_albumartist' in item and item['vt_albumartist'] == self.albumartist:
      return 0
    
    item.try_write()
    item.store()
    return 1
  
  def set_albumartist(self, default_albumartist):
    input_options = None
    if self.albumartist is None or self.albumartist == "":
      self.albumartist = default_albumartist
      input_options = (u'Accept as-is', u'Edit')
      ui.print_(u'Default Virtual Album Artist:')
    else:
      if self.albumartist == default_albumartist:
        input_options = (u'Accept as-is', u'Edit')
      else:
        input_options = (u'Accept as-is', u'Edit', u'Default value')
      ui.print_(u'Current Virtual Album Artist:')
    ui.print_(u'    {}'.format(self.albumartist))
    
    sel = ui.input_options(input_options)
    if sel == u'a':
      pass
    elif sel == u'e':
      self.albumartist = ui.input_(u'Virtual Album Artist:').strip()
    elif sel == u'd':
      self.albumartist = default_albumartist
    else:
      assert False
  
  def _import_after_apply(self, session, task):
    if task.choice_flag != action.APPLY:
      return
    
    self.albumartist = None
    self.should_set = True
    
    for item in task.items:
      if 'vt_albumartist' in item:
        if self.albumartist is None:
          self.albumartist = item['vt_albumartist']
        elif self.albumartist != item['vt_albumartist']:
          self.albumartist = ""
    
    chosen_albumartist = task.chosen_ident()[0]    
    self.set_albumartist(chosen_albumartist)
  
  def _before_write(self, item, path, tags):
    if self.should_set:
      item['vt_albumartist'] = self.albumartist
      tags['vt_albumartist'] = self.albumartist
