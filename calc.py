@dataclass
class Band
    lo: int
    hi: int
    perc: float = 0
    add: int = 0
    
    @property
    def _key(self) -> str:
      return str(sorted(astuple(self)))
    
    def __eq__(self, other) -> bool:
      return self._key == other._key
    
    def __hash__(self) -> int:
      return hash(self._key)
    
    def __le__(self, other) -> bool:
      return self.lo < other.lo

BANDS = [
Band(0,18200),
  Band(18201,45000,19),
  Band(45001,120000,32.5,5092),
  Band(120001, 180000, 37, 29467),
  Band(180001, -1, 45, 51667),
]

# use deduce_super=None if no super should be deduced
def calculate_tax(gross:float, deduce_super:Optional[float]=SUPER_PERC) -> float:
  remainder = gross * ((1-deduce_super/100) if deduce_super is not None else 1)
  while remainder >= 0:
    for band in BANDS:
      if remainder > ...
      remainder -= band.hi

