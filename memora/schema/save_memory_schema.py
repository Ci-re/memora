from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MemoryToStore(BaseModel):
    memory: str
    source_msg_block_pos: list[int] # The position of the message block that resulted in this memory.

class ContraryMemory(MemoryToStore):
    existing_contrary_memory_id: str # The memory_id of the existing memory that was contradicted.

class MemoriesAndInteraction(BaseModel):
    """
    Contains both the interaction and the associated memories to store in memory stores.
    """
    interaction: list[dict[str, str]] # The messages in the interaction [{'role': 'user', 'content': 'hello'}, ...].
    interaction_date: datetime = datetime.now() # The date and time the interaction was saved, defaults to now.
    memories: Optional[list[MemoryToStore]] = [] # The memories extracted from the interaction with their source messages position.
    contrary_memories: Optional[list[ContraryMemory]] = [] # The memory extracted from the interaction with the above but also the memory id of the existing memory they contradicted.
