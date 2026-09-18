# AI Agent

**Fase:** 2 — AI Engineering (LLM)  
**Section:** RAG & AI Agent Development

> Diverifikasi: CrewAI documentation — sumber: https://docs.crewai.com/ — tanggal cek: 2026-09-18
> Diverifikasi: OpenAI Python SDK v3.15.0 — sumber: https://github.com/openai/openai-python/releases — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan chatbot chain, workflow, dan agent;
- merancang tool schema, permission, timeout, dan approval;
- membatasi loop dan context pada agent;
- membangun state machine yang dapat diobservasi;
- mengevaluasi tool selection dan task completion.

## Konteks di PT Kirimin

Pertanyaan customer dapat membutuhkan cek tracking, membaca SOP, atau eskalasi ke finance. Fajar meminta agent yang dapat memilih tool tetapi tidak boleh melakukan refund otomatis.

## Konsep kunci

### Agent loop

**Definisi teknis:** Agent mengobservasi state, memilih action/tool, menerima result, lalu melanjutkan atau berhenti berdasarkan policy. Loop perlu max steps, timeout, and termination condition.

**Penjelasan sederhana:** Agent adalah petugas yang boleh melakukan beberapa langkah, tetapi harus memiliki batas waktu dan supervisor.

### Tool contract dan least privilege

**Definisi teknis:** Tool contract mendefinisikan name, description, typed arguments, result schema, side effects, auth scope, dan error. Tool dengan side effect memerlukan approval/idempotency.

**Penjelasan sederhana:** Memberi agent tombol “lihat status” berbeda dengan tombol “kirim uang”; izin dan konfirmasi harus berbeda.

### Multi-agent

**Definisi teknis:** Multi-agent membagi role/task antar agent, tetapi menambah coordination, latency, cost, dan attack surface. Mulai dari single orchestrator jika cukup.

**Penjelasan sederhana:** Menambah banyak petugas tidak otomatis lebih cepat jika mereka saling mengulang pekerjaan.

## Agent design Kirimin

Router: classify intent. Tools: `get_tracking`, `retrieve_sop`, `create_handoff`. Tidak ada tool refund. Max 4 steps; setiap tool result memiliki trace id; human approval untuk tindakan irreversible.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| CrewAI | verifikasi package pin saat implementasi | multi-agent comparison |
| OpenAI Python SDK | 3.15.0 | tool calling adapter |

## Referensi resmi

- [CrewAI docs](https://docs.crewai.com/)
- [OpenAI function calling](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI Agents SDK overview](https://platform.openai.com/docs/guides/agents)

## Lanjut ke praktik

Notebook menjalankan deterministic agent state machine dengan mock tools.

## Posisi part dalam bootcamp

Part ini memperkenalkan agent sebagai loop yang memilih tool dan langkah untuk menyelesaikan tujuan, bukan sekadar prompt chain. Anda akan memulai dari workflow terbatas agar behavior dapat diuji dan side effect tetap dikendalikan.

## Kapan konsep ini dipakai

Gunakan agent ketika urutan langkah bergantung pada hasil observasi dan jumlah jalur terlalu banyak untuk workflow statis. Gunakan deterministic workflow jika jalurnya diketahui dan reliability lebih penting daripada fleksibilitas. Agent tidak boleh memiliki permission lebih besar daripada kebutuhan task.

## Walkthrough terpandu: triage shipment exception

1. Definisikan goal dan stop condition: cari order, cek latest status, ambil SOP, buat draft action, lalu minta approval.
2. Daftarkan tools dengan JSON schema, description, permission, timeout, dan side-effect label.
3. Beri agent read-only tools terlebih dahulu. Tool write/send harus berada di balik approval gate.
4. Batasi max steps, token, waktu, dan tool call. Simpan state/correlation id.
5. Uji happy path, ambiguous order, tool timeout, conflicting data, prompt injection pada note, dan loop.
6. Validasi tool arguments sebelum eksekusi dan hasil tool sebelum dimasukkan ke context.
7. Evaluasi task success, wrong tool rate, unnecessary steps, escalation quality, latency, dan cost.

## Latihan terbimbing

- Buat agent dengan dua read-only tools.
- Tambahkan planner versus direct tool selection dan bandingkan trace.
- Simulasikan tool yang mengembalikan data berbahaya sebagai text.
- Buat approval UI atau CLI.
- Tambahkan loop detector dan max-step guard.

## Checkpoint penguasaan

Anda siap lanjut jika agent memiliki tools terbatas, stop condition, trace lengkap, guardrail side effect, dan test failure yang menunjukkan sistem berhenti dengan aman.

## Jembatan ke assignment

Assignment harus berisi agent implementation, tool contracts, traces, guardrails, approval flow, test fixtures, dan limitation note.
