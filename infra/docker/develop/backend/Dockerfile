# Build stage
FROM golang:1.22-alpine AS build

WORKDIR /backend

RUN apk add --no-cache \
    git \
    ca-certificates

COPY ./backend/go.mod ./backend/go.sum ./

RUN go mod download

COPY ./backend .

RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /out/api ./cmd/api

# Runtime stage
FROM alpine:3.20

RUN apk add --no-cache \
    ca-certificates \
    tzdata

WORKDIR /luxus-connect/backend

COPY --from=build /out/api /api

ENV PORT=8080

EXPOSE 8080

USER nobody

ENTRYPOINT ["/api"]
