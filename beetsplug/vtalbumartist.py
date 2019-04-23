from beets.plugins import BeetsPlugin
from beets.importer import action
from beets import ui
from beets import mediafile

class VTAlbumArtist(BeetsPlugin):
  def __init__(self):
    super(VTAlbumArtist, self).__init__()
    
    self.should_set = False
    self.albumartist = None
    
    self.register_listener('import_task_choice', self._import_after_apply)
    self.register_listener('write', self._before_write)
    
    field = mediafile.MediaField(
        mediafile.MP3DescStorageStyle(u'VT Album Artist'),
        mediafile.MP4StorageStyle(u'----:com.apple.iTunes:VT Album Artist'),
        mediafile.ASFStorageStyle(u'VT/Album Artist'),
        mediafile.StorageStyle(u'VT_ALBUMARTIST')
    )
    self.add_media_field('vt_albumartist', field)
    
  def _import_after_apply(self, session, task):
    if task.choice_flag == action.APPLY:
      albumartist = task.chosen_ident()[0]
      
      ui.print_(u'Default Virtual Album Artist:')
      ui.print_(u'    {}'.format(albumartist))
        
      sel = ui.input_options( (u'Accept as-is', u'Edit') )
      if sel == u'a':
        self.albumartist = albumartist
      elif sel == u'e':
        self.albumartist = ui.input_(u'Virtual Album Artist:').strip()
      else:
        assert False
      
      self.should_set = True
  
  def _before_write(self, item, path, tags):
    if self.should_set:
      item['vt_albumartist'] = self.albumartist
      tags['vt_albumartist'] = self.albumartist
