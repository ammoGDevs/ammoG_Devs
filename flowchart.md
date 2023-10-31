graph TD
  A[Start] --> B[Process 1]
  B --> C[Process 2]
  C --> D[Decision]
  D -- Yes --> E[Process 3]
  D -- No --> F[Process 4]
  E --> G[End]
  F --> G
