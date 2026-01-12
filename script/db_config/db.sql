CREATE TABLE error_logs (
    id          BIGSERIAL PRIMARY KEY,
    timestamp   TIMESTAMPTZ NOT NULL DEFAULT now(),
    exception   TEXT NOT NULL,    -- eccezione completa
);