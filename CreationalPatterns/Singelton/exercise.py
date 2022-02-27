def is_singleton(factory):
   factory1 = factory()
   factory2 = factory()
   return factory1 is factory2