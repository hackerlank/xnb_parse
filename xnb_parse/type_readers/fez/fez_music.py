"""
FEZ music type readers
"""

from xnb_parse.type_reader import BaseTypeReader, ValueTypeReader
from xnb_parse.type_reader_manager import TypeReaderPlugin
from xnb_parse.type_readers.xna_system import ListReader, ArrayReader, EnumReader
from xnb_parse.type_readers.xna_primitive import Int32Reader


class TrackedSongReader(BaseTypeReader, TypeReaderPlugin):
    target_type = u'FezEngine.Structure.TrackedSong'
    reader_name = u'FezEngine.Readers.TrackedSongReader'

    def read(self):
        loops = self.stream.read_object(ListReader, [LoopReader])
        name = self.stream.read_string()
        tempo = self.stream.read_int32()
        time_signature = self.stream.read_int32()
        notes = self.stream.read_object(ArrayReader, [ShardNotesReader])
        assemble_chord = self.stream.read_object(EnumReader, [AssembleChordsReader])
        random_ordering = self.stream.read_boolean()
        custom_ordering = self.stream.read_object(ArrayReader, [Int32Reader])
        return loops, name, tempo, time_signature, notes, assemble_chord, random_ordering, custom_ordering


class LoopReader(BaseTypeReader, TypeReaderPlugin):
    target_type = u'FezEngine.Structure.Loop'
    reader_name = u'FezEngine.Readers.LoopReader'

    def read(self):
        duration = self.stream.read_int32()
        loop_times_from = self.stream.read_int32()
        loop_times_to = self.stream.read_int32()
        name = self.stream.read_string()
        trigger_from = self.stream.read_int32()
        trigger_to = self.stream.read_int32()
        delay = self.stream.read_int32()
        night = self.stream.read_boolean()
        day = self.stream.read_boolean()
        dusk = self.stream.read_boolean()
        dawn = self.stream.read_boolean()
        fractional_time = self.stream.read_boolean()
        one_at_a_time = self.stream.read_boolean()
        cut_off_tail = self.stream.read_boolean()
        return (duration, loop_times_from, loop_times_to, name, trigger_from, trigger_to, delay, night, day, dusk,
                dawn, fractional_time, one_at_a_time, cut_off_tail)


class ShardNotesReader(ValueTypeReader, TypeReaderPlugin):
    target_type = u'FezEngine.Structure.ShardNotes'
    reader_name = u'FezEngine.Readers.ShardNotesReader'

    def read(self):
        return self.stream.read_int32()


class AssembleChordsReader(ValueTypeReader, TypeReaderPlugin):
    target_type = u'FezEngine.Structure.AssembleChords'
    reader_name = u'FezEngine.Readers.AssembleChordsReader'

    def read(self):
        return self.stream.read_int32()